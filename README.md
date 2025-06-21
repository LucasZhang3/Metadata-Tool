# File Metadata Tool

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/streamlit-v1.0+-green.svg)](https://streamlit.io/)  


## Overview

The **File Metadata Tool** is a lightweight web app built with **Streamlit** that allows you to:

**Extract metadata** from images (JPG, PNG), PDFs, and Word documents (DOCX)  
**Remove metadata** to protect your privacy before sharing files

Metadata can include hidden information such as author, creation/modification dates, GPS location, and more.


## Requirements

Python 3.7 or higher  
[Streamlit](https://streamlit.io/)  
[python-docx](https://python-docx.readthedocs.io/en/latest/)  
[pikepdf](https://pikepdf.readthedocs.io/en/latest/)  
[ExifTool](https://exiftool.org/) installed and available on your system PATH  

### Install Python packages

```bash
pip install streamlit python-docx pikepdf
```

### Install ExifTool
Windows: Download and install from exiftool.org

MacOS: Use Homebrew brew install exiftool

Linux: Use your package manager, e.g., sudo apt install libimage-exiftool-perl

## How to Use
Clone this repo or download metadata_tool_app.py.

Open a terminal and run:

streamlit run metadata_tool_app.py
In the web app, upload a supported file (JPG, PNG, PDF, DOCX).

Select either Extract Metadata or Strip Metadata.

View extracted metadata or download the cleaned file.

## Demo
![image](https://github.com/user-attachments/assets/6d2365f1-6cff-45a2-9fb2-b6dc3a230e07)
![image](https://github.com/user-attachments/assets/e74a34b0-1676-4350-89e1-8b20eec267d5)


## Notes
Metadata extraction and removal currently supports JPG, PNG, PDF, and DOCX formats.

Cleaning images modifies the original file in-place, while PDFs and DOCX generate cleaned copies.

Make sure exiftool is installed and accessible from your command line for image metadata operations.

