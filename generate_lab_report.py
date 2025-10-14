import os
import random
from docx import Document
from docx.shared import Pt
from docx2pdf import convert # Optional: for PDF generation

def generate_lab_report():
    doc = Document()
    
    # Leave 10 blank lines for photo/name
    for _ in range(10):
        doc.add_paragraph('')

    # Ensure 'output' directory exists
    if not os.path.exists('output'):
        os.makedirs('output')

    for i, filename in enumerate(sorted(os.listdir('lab_folder'))):
        if not filename.endswith('.c'):
            continue
        
        question_title = os.path.splitext(filename)[0]
        
        # Read code from .c file
        with open(os.path.join('lab_folder', filename), 'r') as f:
            code_content = f.read()

        # Add question title
        p = doc.add_paragraph(f"Question {i+1}: {question_title}")
        p.runs[0].bold = True
        p.runs[0].font.size = Pt(12)
        p.runs[0].font.name = 'Times New Roman'

        # Add code in monospace
        p = doc.add_paragraph()
        run = p.add_run(code_content)
        run.font.name = 'Courier New'
        run.font.size = Pt(10)

        # Add testcase table
        table = doc.add_table(rows=1, cols=2)
        for j in range(2):
            # Random numbers between 5-25 as per roadmap
            val = random.randint(5, 25) 
            table.cell(0, j).text = f"Testcase {j+1}\nInput: {val}\nOutput: __________"
            for paragraph in table.cell(0, j).paragraphs:
                for run_cell in paragraph.runs:
                    run_cell.font.name = 'Courier New'
                    run_cell.font.size = Pt(10)

        doc.add_page_break()

    output_docx_path = os.path.join('output', 'lab_report.docx')
    doc.save(output_docx_path)
    print(f"Lab report saved to {output_docx_path}")

    # Optional: Generate PDF automatically
    try:
        output_pdf_path = os.path.join('output', 'lab_report.pdf')
        convert(output_docx_path, output_pdf_path)
        print(f"Lab report also converted to PDF: {output_pdf_path}")
    except Exception as e:
        print(f"Could not convert to PDF. Make sure LibreOffice or Microsoft Word is installed and accessible: {e}")

if __name__ == "__main__":
    generate_lab_report()