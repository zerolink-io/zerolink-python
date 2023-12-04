"""
Read data files for ingestion into the knowledge graph.
"""

import io
import sys

try:
    from docx import Document
except ImportError:
    NO_DOCX = True

# try:
#    from openpyxl import load_workbook
# except ImportError:
#    NO_XLSX = True


def read_text(path: str) -> str:
    """
    Read the text file
    """
    with open(path, "r") as f:
        return f.read()


def read_docx(path: str) -> str:
    """
    Turn the Microsoft Word document into a raw bytestring
    """
    if NO_DOCX:
        print("Microsoft Word document support is not available")
        sys.exit(1)

    document = Document(path)
    target_stream = io.StringIO()
    for paragraph in document.paragraphs:
        target_stream.write(paragraph.text + "\n")
    return target_stream.getvalue()
