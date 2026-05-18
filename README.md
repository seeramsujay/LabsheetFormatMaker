# 📝 LabsheetFormatMaker: C Compilation, Testcase Runner & High-Fidelity Word/PDF Report Generator

> Instantly convert a folder of raw `.c` files into a beautifully formatted, fully executed, and styled lab report (`.docx`/`.pdf`).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg?style=flat-square)](https://www.python.org/)
[![Compilation](https://img.shields.io/badge/Compiler-GCC-darkgreen.svg?style=flat-square)](https://gcc.gnu.org/)
[![Word Generation](https://img.shields.io/badge/Word--Engine-python--docx-blueviolet.svg?style=flat-square)](https://python-docx.readthedocs.io/)

LabsheetFormatMaker is an automated, student-friendly developer tool engineered to **compile, execute, test, and style university programming lab sheets**. Instead of spending hours manually copying code, indenting text, running programs, taking screenshots, and building Word tables, LabsheetFormatMaker automates the entire lifecycle.

Point the tool at a directory of `.c` files, and it will:
1.  **Compile** each file dynamically using `gcc`.
2.  **Actuate sandboxed subprocesses** with randomly generated test inputs (within customized domains).
3.  **Capture and clean stdout/stderr streams** (intelligently isolating user prompts from actual execution output).
4.  **Synthesize a highly formatted Microsoft Word document (`.docx`)** with narrow margins, custom fonts (Times New Roman & Courier New), structured code boxes, and dual-column testcase execution matrices.
5.  **Convert the document to PDF** instantly for immediate submission.

---

## ⚙️ How the Pipeline Works

```mermaid
flowchart TD
    subgraph Input Layer [Sources]
        A["lab_folder/ (*.c)"] -->|Scan Files| B["Directory Parser"]
    end
    
    subgraph Execution Layer [Compilation & Testing]
        B -->|GCC Compilation| C["Binary Executables"]
        C -->|Inject Random Inputs [5-25]| D["Subprocess Runner"]
        D -->|Capture & Strip Prompts| E["Structured Stdout/Stderr Logs"]
    end
    
    subgraph Formatting Layer [Document Synthesis]
        E & B -->|python-docx Builder| F["Word Styling Engine"]
        F -->|Borders & Page Layouts| G["lab_report.docx"]
    end
    
    subgraph Output Layer [Publishing]
        G -->|docx2pdf Converter| H["lab_report.pdf"]
    end
```

---

## ⚡ Core Features

*   **Sandboxed Auto-Execution:** Compiles code on-the-fly and tests it. No need to run programs manually to copy outputs.
*   **Prompt-Isolation Algorithm:** Identifies common console prompt suffixes (e.g., `"Enter a number: "`) and strips them from testcase output cards, keeping the output clean and professional.
*   **Courier New Code Blocks:** Wraps code in monospace Courier New blocks inside single-cell border tables, preserving perfect C indentations, spaces, and brackets.
*   **Times New Roman Question Titles:** Renders academic question headers in structured Times New Roman, matching standard university lab formats.
*   **Dual-Column Testcase Matrices:** Generates comparative adjacent testcase blocks with custom inputs and their respective runtime outputs.

---

## 📐 Document Spacing & Typography Specifications

| Section | Description | Font & Size | Border / Styling |
| :--- | :--- | :--- | :--- |
| **Cover Buffer** | ~10 empty lines at the top of page 1 | Times New Roman | Spacing for photos, names, and IDs |
| **Question Title** | `"Question N: <FileName>"` | **Times New Roman, 12pt, Bold** | Part of the main code container |
| **Code Box** | The raw `.c` file source code | **Courier New, 10pt** | Monospace container with single solid black borders |
| **Testcase Matrix** | Side-by-side execution cards | **Courier New, 10pt** | Dual columns with custom input & captured output |

---

## 🚀 Quick Start (Under 30 Seconds)

### 1. Install System Tools
Ensure you have `gcc` (GNU Compiler Collection) and Python 3.12+ installed on your system.

### 2. Install Python Dependencies
Clone this repository and install `python-docx` along with `docx2pdf`:

```bash
git clone https://github.com/seeramsujay/LabsheetFormatMaker.git
cd LabsheetFormatMaker
pip install python-docx docx2pdf
```

### 3. Load Your C Files
Place all your `.c` source files inside the `lab_folder/` directory:

```bash
ls lab_folder/
# Output: Factorial.c  Fibonacci.c  PrimeCheck.c
```

### 4. Build Your Report
Run the automation script to generate your report:

```bash
python generate_lab_report.py
```
This compiles every C file, runs the test cases, formats the DOCX, and builds:
*   `output/lab_report.docx` (editable Microsoft Word report)
*   `output/lab_report.pdf` (print-ready PDF file)

---

## 📁 Repository Layout

*   `lab_folder/`: Folder where your `.c` files reside. The filename dictates the question title.
*   `output/`: Contains the generated report outputs and temporary compilation binaries.
*   `generate_lab_report.py`: The core compiler, subprocess driver, and document writer.
*   `Lab Report_format.docx`: The baseline reference layout.

---

## 📄 License

This project is licensed under the **MIT License**. See `LICENSE` for details.