import streamlit as st
import subprocess
import pikepdf
from docx import Document
import os
import tempfile

st.set_page_config(page_title="File Metadata Tool", layout="centered")

st.title("File Metadata Tool")
st.write(
    "Upload an image (JPG, PNG), PDF, or Word document (DOCX) to either extract metadata or remove it."
)

st.markdown(
    """
    ### Actions:
    - **Extract Metadata:** Reads and displays hidden information in your file such as author, creation date, GPS location (for images), and more.
    - **Strip Metadata:** Removes all metadata from your file to protect your privacy before sharing. The cleaned file can be downloaded.
    """
)

uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png", "pdf", "docx"])
action = st.radio("Choose action", ["Extract Metadata", "Strip Metadata"])

def extract_exif(file_path):
    result = subprocess.run(["exiftool", file_path], capture_output=True, text=True)
    return result.stdout

def extract_pdf_metadata(file_path):
    with pikepdf.open(file_path) as pdf:
        return dict(pdf.docinfo)

def extract_docx_metadata(file_path):
    doc = Document(file_path)
    core_props = doc.core_properties
    return {
        "author": core_props.author,
        "title": core_props.title,
        "created": str(core_props.created),
    }

def strip_exif(file_path):
    subprocess.run(["exiftool", "-all=", "-overwrite_original", file_path])
    return file_path

def strip_pdf_metadata(file_path):
    output_path = file_path.replace(".pdf", "_clean.pdf")
    with pikepdf.open(file_path) as pdf:
        pdf.save(output_path)
    return output_path

def strip_docx_metadata(file_path):
    doc = Document(file_path)
    core_props = doc.core_properties
    core_props.author = ""
    core_props.title = ""
    output_path = file_path.replace(".docx", "_clean.docx")
    doc.save(output_path)
    return output_path

if uploaded_file:
    suffix = os.path.splitext(uploaded_file.name)[-1].lower()
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    if action == "Extract Metadata":
        st.subheader("Extracted Metadata")
        try:
            if suffix in [".jpg", ".jpeg", ".png"]:
                metadata = extract_exif(tmp_path)
                st.text(metadata)
            elif suffix == ".pdf":
                metadata = extract_pdf_metadata(tmp_path)
                st.json(metadata)
            elif suffix == ".docx":
                metadata = extract_docx_metadata(tmp_path)
                st.json(metadata)
            else:
                st.error("Unsupported file type.")
        except Exception as e:
            st.error(f"Error extracting metadata: {e}")

    elif action == "Strip Metadata":
        st.subheader("Cleaned File")
        try:
            if suffix in [".jpg", ".jpeg", ".png"]:
                strip_exif(tmp_path)
                st.download_button(
                    "Download Cleaned File",
                    data=open(tmp_path, "rb").read(),
                    file_name="clean_" + uploaded_file.name,
                )
            elif suffix == ".pdf":
                output_path = strip_pdf_metadata(tmp_path)
                st.download_button(
                    "Download Cleaned PDF",
                    data=open(output_path, "rb").read(),
                    file_name="clean_" + uploaded_file.name,
                )
            elif suffix == ".docx":
                output_path = strip_docx_metadata(tmp_path)
                st.download_button(
                    "Download Cleaned DOCX",
                    data=open(output_path, "rb").read(),
                    file_name="clean_" + uploaded_file.name,
                )
            else:
                st.error("Unsupported file type.")
        except Exception as e:
            st.error(f"Error stripping metadata: {e}")
