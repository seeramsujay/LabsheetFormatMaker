Let’s design your project **from scratch** now that you’re switching from CSV → `.c` files, with a clear **roadmap**, explanation of **how** to do each step, and **what language** is best for this automation task.

---

# 🧭 Project Goal

> “Automatically generate a lab report Word document (`.docx`) that follows a fixed format — includes question titles, C source code (preserving indentation), and random test cases — from a folder of `.c` files.”

You’ll add your **photo manually** later, and the report must use **Courier New** everywhere for uniformity.

---

## 🧰 1️⃣ Choose the right programming language


Use **Python** — it balances **simplicity, power, and portability**, and is easiest to maintain and debug.

---

## 🪜 2️⃣ Project Roadmap (step-by-step)

### **Step 1: Prepare the Folder**

```
lab_folder/
├── Factorial.c
├── PrimeCheck.c
├── Fibonacci.c

```

Each `.c` file’s name = question title.

---

### **Step 2: Set Up the Environment**

1. Install Python = 3.12
2. Install dependencies:

   ```bash
   pip install python-docx pandas
   ```

---

### **Step 3: Plan the Document Layout**

For each `.c` file, the script will generate:

| Section        | Description                    | Font / Style                                            |
| -------------- | ------------------------------ | ------------------------------------------------------- |
| Blank space    | ~10 empty lines for photo/name | Times New Roman (default) (Only once)                   |
| Question       | “Question n: <filename>”       | Bold, 12pt, Times New Roman                             |
| Code           | Contents of `.c` file          | **Courier New**, 10pt, monospace, indentation preserved |
| Testcase table | 1 row × 2 columns              | Courier New, 10pt    Random numbers between 5-25        | 

Example structure in Word:

```
(10 blank lines)

Question 1: Factorial
Code:
<indented C code>

Testcase 1 | Testcase 2
Input: 4   | Input: 7
Output: ____ | Output: ____

Question 2: Prime
Code:
<indented C code>

Testcase 1 | Testcase 2
Input: 5   | Input: 8
Output: ____ | Output: ____
```

---

### **Step 4: Build the Script (Python)**

High-level logic:

```python
import os, random
from docx import Document
from docx.shared import Pt

doc = Document()
# leave 10 blank lines
for _ in range(10):
    doc.add_paragraph('')

for i, filename in enumerate(sorted(os.listdir('lab_folder'))):
    if not filename.endswith('.c'):
        continue
    question = os.path.splitext(filename)[0]
    code = open(os.path.join('lab_folder', filename)).read()

    # Add question title
    p = doc.add_paragraph(f"Question {i+1}: {question}")
    p.runs[0].bold = True

    # Add code in monospace
    p = doc.add_paragraph()
    run = p.add_run(code)
    run.font.name = 'Courier New'
    run.font.size = Pt(10)

    # Add testcase table
    table = doc.add_table(rows=1, cols=2)
    for j in range(2):
        val = random.randint(1, 100)
        table.cell(0, j).text = f"Testcase {j+1}\nInput: {val}\nOutput: __________"

    doc.add_page_break()

doc.save('lab_report.docx')
```

This preserves your indentation because:

* Reading `.c` file as plain text keeps spaces and newlines.
* `python-docx` doesn’t strip them if you don’t split lines manually.
* Using Courier New ensures alignment.

---

### **Step 5: Verify Formatting**

* Open the generated `lab_report.docx`
* Check:

  * Spacing looks same as your `Lab Report_format.docx`
  * Indentation preserved
  * Font = Courier New for code/testcases
* Adjust font sizes or spacing if needed.

---

### **Step 6: Polish (Optional Add-ons)**

| Feature                            | How to Add                                                               |
| ---------------------------------- | ------------------------------------------------------------------------ |
| Add header/footer                  | `doc.sections[0].footer.paragraphs[0].text = "Lab Report number <given>"`|
| Auto numbering questions           | Already supported                                                        |
| Insert random test cases per range | range between 5 and 15 (run code in a cell (code is in gcc clanguage))   |
| Generate PDF automatically         | Add `from docx2pdf import convert` and call `convert("lab_report.docx")` |

---

### **Step 7: Run Anytime**

You can just drop new `.c` files in the folder and rerun:

```bash
python generate_lab_report.py
```

It will automatically rebuild the `.docx`.

---

## 🧱 Directory Summary (Final)

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

---

## 🏁 Final Verdict

| Goal                                               | Best Language                 | Reason                                                        |
| -------------------------------------------------- | ----------------------------- | ------------------------------------------------------------- |
| Automate lab report creation from `.c` files       | **Python**                    | Powerful `python-docx`, preserves indentation, simple to code |
| Require perfect Word fidelity + Office integration | **C#**                        | Full OpenXML control but heavy setup                          |
| Need to run from a web UI                          | **Node.js or Flask (Python)** | Extend the same code with API                                 |

✅ **Use Python**, because it’s the right balance of simplicity, flexibility, and formatting control.

---