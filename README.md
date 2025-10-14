# Lab Report Generator

This project automates the generation of lab reports from `.c` files, creating a Word document (`.docx`) with a fixed format. The report includes question titles, C source code (preserving indentation), and random test cases.

## Project Goal

> Automatically generate a lab report Word document (`.docx`) that follows a fixed format — includes question titles, C source code (preserving indentation), and random test cases — from a folder of `.c` files.

## Roadmap

1.  **Choose the right programming language:** Python is recommended for its simplicity, power, and portability.
2.  **Project Roadmap (step-by-step):**
    *   **Step 1: Prepare the Folder:** Organize your `.c` files in a folder (e.g., `lab_folder/`). Each `.c` file's name will be used as the question title.
    *   **Step 2: Set Up the Environment:**
        *   Install Python 3.12 or later.
        *   Install the required dependencies:
            ```bash
            pip install python-docx pandas
            ```
    *   **Step 3: Plan the Document Layout:** The script generates a section for each `.c` file with the following structure:

        | Section        | Description                    | Font / Style                                            |
        | -------------- | ------------------------------ | ------------------------------------------------------- |
        | Blank space    | ~10 empty lines for photo/name | Times New Roman (default) (Only once)                   |
        | Question       | “Question n: <filename>”       | Bold, 12pt, Times New Roman                             |
        | Code           | Contents of `.c` file          | **Courier New**, 10pt, monospace, indentation preserved |
        | Testcase table | 1 row × 2 columns              | Courier New, 10pt    Random numbers between 5-25        |

    *   **Step 4: Build the Script (Python):** A Python script (`generate_lab_report.py`) automates the process.
    *   **Step 5: Verify Formatting:** Open the generated `lab_report.docx` and check the spacing, indentation, and fonts.
    *   **Step 6: Polish (Optional Add-ons):** Add features like headers/footers, auto-numbering questions, insert random test cases per range or generate PDF automatically.
    *   **Step 7: Run Anytime:** Place new `.c` files in the folder and rerun the script to rebuild the `.docx`.

## Directory Structure

```
project_root/
├── Lab Report_format.docx       # template reference
├── generate_lab_report.py       # Python script
├── lab_folder/                  # folder with your .c files
│   ├── Factorial.c
│   ├── PrimeCheck.c
│   ├── Fibonacci.c
│   └── ...
└── output/
    └── lab_report.docx
```

## Final Verdict

Python is the recommended language for automating lab report creation due to its powerful `python-docx` library, ability to preserve indentation, and ease of coding.