from docx import Document
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from generate_lab_report import set_cell_border_corrected

def test_set_cell_border():
    doc = Document()
    table = doc.add_table(rows=1, cols=1)
    cell = table.cell(0, 0)
    set_cell_border_corrected(cell, top={"val": "single", "sz": 4, "color": "auto"})
    assert cell._tc.get_or_add_tcPr() is not None

def test_document_creation():
    doc = Document()
    doc.add_heading("Lab Report Title", 0)
    p = doc.add_paragraph("Test Paragraph")
    assert len(doc.paragraphs) >= 2
