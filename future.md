# LabsheetFormatMaker: Architectural Review & Academic Automation Roadmap (future.md)

---

## 1. Architectural Code Review & Current State Analysis

LabsheetFormatMaker automates the tedious university lab reporting lifecycle. It dynamically scans directories of `.c` source files, compiles them via `gcc`, actuates sandboxed testcase executions with randomized domain inputs, isolates user prompt strings from real execution outputs, and synthesizes styled Microsoft Word (`.docx`) and `.pdf` reports complete with narrow margins, Courier New monospace code containers, and dual-column testcase execution matrices.

### Architectural Strengths
- **Prompt-Isolation Heuristic:** Distinguishes interactive terminal prompts (e.g. `"Enter n: "`) from program calculation output, preventing prompt pollution in final reports.
- **Academic Standard Formatting:** Renders Times New Roman headers alongside framed Courier New source listings and side-by-side test cards.
- **Zero-Touch PDF Compilation:** Uses `docx2pdf` to deliver final ready-to-submit PDF documents without manual Word interaction.

### Identified Bottlenecks & Modernization Needs
1. **Single-Language (C) Confinement:** Pipeline currently targets only `.c` files via GCC, lacking support for C++, Python, Java, Rust, or MATLAB assignments.
2. **Platform DOCX-to-PDF Dependency:** `docx2pdf` relies on Microsoft Word COM automation on Windows or LibreOffice on Linux, which can fail silently on minimal CI container environments.
3. **Absence of Memory Leak & Static Analysis:** The tool executes programs but does not check for memory leaks (`valgrind`), buffer overflows, or compiler warnings (`-Wall -Wextra`).

---

## 2. Strategic Engineering Roadmap

```mermaid
flowchart TD
    subgraph Phase 1: Polyglot Execution & Static Analysis
        P1A[Polyglot Compiler: C++, Python, Java, Rust] --> P1B[Valgrind & ASan Memory Leak Checker]
        P1B --> P1C[Automated Compiler Warning Scoring]
    end

    subgraph Phase 2: Modern Typst & LaTeX Engine
        P2A[Typst Native Document Compiler] --> P2B[Sub-50ms PDF Rendering Engine]
        P2B --> P2C[Publication-Grade Code Syntax Highlighting]
    end

    subgraph Phase 3: WebAssembly Browser Studio
        P3A[WebAssembly Sandboxed C Engine: Wasm-Clang] --> P3B[Drag-and-Drop Browser Workspace]
        P3B --> P3C[Zero-Install Instant Report Generator]
    end

    subgraph Phase 4: Plagiarism & AI Boilerplate Detector
        P4A[Moss / AST Similarity Tokenizer] --> P4B[Academic Integrity Pre-Submission Check]
        P4B --> P4C[Personalized Styling & University Template Packs]
    end

    Phase 1 --> Phase 2
    Phase 2 --> Phase 3
    Phase 3 --> Phase 4
```

---

## 3. Detailed Milestone Execution Plan

### Milestone 1: Multi-Language Compilation & Memory Safety
- [ ] **Polyglot Execution Runner:** Extend `generate_lab_report.py` to auto-detect language by file extension (`.cpp` $\to$ `g++`, `.py` $\to$ `python3`, `.rs` $\to$ `rustc`, `.java` $\to$ `javac`).
- [ ] **AddressSanitizer (ASan) & Valgrind Ingestion:** Automatically run binaries with `-fsanitize=address` to flag segmentation faults or memory leaks directly in the testcase matrix.
- [ ] **Compiler Warning Annotations:** Highlight code lines triggering `-Wall` warnings directly inside the generated report.

### Milestone 2: Modern Typst PDF Engine
- [ ] **Typst Template Integration:** Replace fragile `docx2pdf` COM automation with Typst, compiling high-fidelity PDF reports with native syntax highlighting in $<50\text{ms}$.
- [ ] **Modular University Style Packs:** Provide pre-built configuration presets for major university formats (VTU, JNTU, Anna University, IEEE standard).

### Milestone 3: In-Browser WebAssembly Studio
- [ ] **Wasm Compiler Core:** Run clang and execution sandboxes directly in the browser via WebAssembly, allowing students to generate lab sheets without installing GCC locally.
- [ ] **Real-time Live Preview:** Interactive dual-pane editor showing the source code and generated PDF side-by-side with live updates.

### Milestone 4: Academic Integrity & Plagiarism Checker
- [ ] **Local AST Tokenizer:** Compare student code against past repository submissions to detect code duplication and accidental variable-renaming plagiarism.
- [ ] **Custom Watermarking & Roll Number Stamps:** Automatically embed university roll numbers and cryptographic timestamps into PDF footer watermarks.
