import os
import random
import subprocess
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml.shared import OxmlElement # Import OxmlElement
from docx.shared import Inches
from docx2pdf import convert # Optional: for PDF generation

# Corrected set_cell_border function
def set_cell_border_corrected(cell, **kwargs):
    """
    Set cell border properties.
    """
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()

    # Get or add the tcBorders element
    tcBorders = tcPr.first_child_found_in("w:tcBorders")
    if tcBorders is None:
        tcBorders = OxmlElement("w:tcBorders")
        tcPr.append(tcBorders)

    # Define border attributes
    for border_name, border_value in kwargs.items():
        # Use the unqualified tag name with prefix for OxmlElement
        unqualified_tag = f'w:{border_name}'
        
        # Remove existing border element if it exists
        existing_border = tcBorders.find(qn(unqualified_tag)) # Use qn for finding existing elements
        if existing_border is not None:
            tcBorders.remove(existing_border)
        
        new_border = OxmlElement(unqualified_tag) # Corrected: Pass unqualified tag directly
        new_border.set(qn('w:val'), border_value.get('val', "single"))
        new_border.set(qn('w:sz'), str(border_value.get('sz', 4))) # 0.5 point (4 eighths of a point)
        new_border.set(qn('w:space'), str(border_value.get('space', 0)))
        new_border.set(qn('w:color'), border_value.get('color', "auto"))
        tcBorders.append(new_border)


def generate_lab_report():
    doc = Document()
    
    # Set page margins to narrow (0.5 inches all around)
    section = doc.sections[0]
    section.top_margin = Inches(0.5)
    section.bottom_margin = Inches(0.5)
    section.left_margin = Inches(0.5)
    section.right_margin = Inches(0.5)

    # Leave 10 blank lines for photo/name
    for _ in range(10):
        doc.add_paragraph('')

    # Ensure 'output' directory exists
    if not os.path.exists('output'):
        os.makedirs('output')

    for i, filename in enumerate(sorted(os.listdir('lab_folder'))):
        if not filename.endswith('.c'):
            continue
        
        c_file_path = os.path.join('lab_folder', filename)
        question_title = os.path.splitext(filename)[0]
        
        # Read code from .c file
        with open(c_file_path, 'r') as f:
            code_content = f.read()

        # --- Add Question and Code in a Box (Table) ---
        question_code_table = doc.add_table(rows=2, cols=1)
        question_code_table.autofit = False
        question_code_table.columns[0].width = Inches(7) # Adjusted width for narrow margins

        # Question Row
        q_cell = question_code_table.cell(0, 0)
        p_q = q_cell.add_paragraph(f"Question {i+1}: {question_title}")
        p_q.runs[0].bold = True
        p_q.runs[0].font.size = Pt(12)
        p_q.runs[0].font.name = 'Times New Roman'
        p_q.alignment = WD_ALIGN_PARAGRAPH.LEFT

        # Code Row
        c_cell = question_code_table.cell(1, 0)
        p_c = c_cell.add_paragraph("Code:")
        p_c.runs[0].bold = True
        p_c.runs[0].font.size = Pt(10)
        p_c.runs[0].font.name = 'Times New Roman'
        p_c.alignment = WD_ALIGN_PARAGRAPH.LEFT

        p_code = c_cell.add_paragraph()
        run_code = p_code.add_run(code_content)
        run_code.font.name = 'Courier New'
        run_code.font.size = Pt(10)
        p_code.alignment = WD_ALIGN_PARAGRAPH.LEFT

        # Apply borders to the cells
        for row in question_code_table.rows:
            for cell in row.cells:
                set_cell_border_corrected(
                    cell,
                    top={'sz': 12, 'val': 'single', 'color': '#000000'},
                    left={'sz': 12, 'val': 'single', 'color': '#000000'},
                    bottom={'sz': 12, 'val': 'single', 'color': '#000000'},
                    right={'sz': 12, 'val': 'single', 'color': '#000000'},
                )
        doc.add_paragraph('') # Add a blank line after the box

        # --- Compile and Execute C code ---
        executable_name = os.path.splitext(filename)[0]
        executable_path = os.path.join('output', executable_name)

        # --- Compile C code ---
        executable_name = os.path.splitext(filename)[0]
        executable_path = os.path.join('output', executable_name)
        
        compile_result = subprocess.run(
            ['gcc', c_file_path, '-o', executable_path],
            capture_output=True,
            text=True
        )

        # --- Add testcase table ---
        table = doc.add_table(rows=1, cols=2)
        table.autofit = False
        table.columns[0].width = Inches(3.5) # Adjusted width for narrow margins
        table.columns[1].width = Inches(3.5) # Adjusted width for narrow margins

        for j in range(2):
            val = random.randint(5, 25)
            execution_output = "Error: Could not compile or run C code."

            if compile_result.returncode != 0:
                execution_output = f"Compilation Error:\n{compile_result.stderr}"
            else:
                # Execute with input
                run_result = subprocess.run(
                    [executable_path],
                    input=str(val), # Pass the random value as stdin
                    capture_output=True,
                    text=True
                )
                # Extract only the relevant output (e.g., after "Enter a number: ")
                program_output_lines = run_result.stdout.strip().split('\n')
                if program_output_lines and "Enter a number:" in program_output_lines[0]:
                    execution_output = "\n".join(program_output_lines[1:])
                else:
                    execution_output = run_result.stdout.strip()
            
            cell_text = f"Testcase {j+1}\nInput: {val}\nOutput: {execution_output}"
            cell = table.cell(0, j)
            cell.text = cell_text
        
        # Clean up executable after all test cases for this file are done
        if os.path.exists(executable_path):
            os.remove(executable_path)
            for paragraph in cell.paragraphs:
                for run_cell in paragraph.runs:
                    run_cell.font.name = 'Courier New'
                    run_cell.font.size = Pt(10)
            
            # Apply borders to testcase cells
            set_cell_border_corrected(
                cell,
                top={'sz': 12, 'val': 'single', 'color': '#000000'},
                left={'sz': 12, 'val': 'single', 'color': '#000000'},
                bottom={'sz': 12, 'val': 'single', 'color': '#000000'},
                right={'sz': 12, 'val': 'single', 'color': '#000000'},
            )


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