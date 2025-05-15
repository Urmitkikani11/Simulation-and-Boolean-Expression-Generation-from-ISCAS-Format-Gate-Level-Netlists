# ISCAS Netlist Simulation and Boolean Expression Generator

This project implements a **Gate-Level Logic Simulation Tool** using Python. It supports **ISCAS-format netlists** and provides both **simulation outputs** and **Boolean expressions** for output nodes. Ideal for educational use, this tool helps understand digital circuit behavior at the gate level.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## 📘 Project Summary

- **Title**: Simulation and Boolean Expression Generation from ISCAS-Format Gate-Level Netlists  
- **Technology**: Python (standard library only)  
- **Authors**:   Urmit Kikani (22BEC137)  
- **Institution**: Nirma University, Institute of Technology  
- **Submitted for**: Testing and Verification of Digital Circuits (TVDC)

---

## ⚙️ Features

-  Parses [ISCAS-format gate-level netlists](ISCAS%20netlists%20for%20an%20input/)
-  Identifies **primary inputs and output nodes**
-  Performs **logic simulation** for given input vectors
-  Generates **Boolean expressions** for output nets
-  CLI-based input prompts for interactive simulation

---

## 🔬 Simulation Workflow

### 1. Load and Parse Netlist
- Reads a `.txt` netlist file with ISCAS gate-level formatting
- Builds internal circuit representation using Python dictionaries

### 2. Input Assignment
- Prompts user to assign binary values (0 or 1) to all **primary input nodes**

### 3. Logic Simulation
- Evaluates each node in the circuit using logic functions:
  - AND, OR, NAND, NOR, NOT, XOR, XNOR, FANOUT
- Simulates the full circuit and propagates signal values

### 4. Expression Generation
- For each output node, builds a **recursive Boolean expression**
- Reflects logical dependencies from inputs to outputs

---

## 📂 Files Included

- [`Code/NetSimLogic.py`](Code/NetSimLogic.py) — Core Python implementation for netlist parsing, simulation, and Boolean expression generation  
- [`ISCAS netlists for an input/c17_iscas2.txt`](ISCAS%20netlists%20for%20an%20input/c17_iscas2.txt) — Sample C17 ISCAS benchmark circuit  
- [`ISCAS netlists for an input/iscas1.txt`](ISCAS%20netlists%20for%20an%20input/iscas1.txt) — Additional ISCAS netlist example  
- [`Report/22BEC137_TVDC_Report.pdf`](Report/22BEC137_TVDC_Report.pdf) — Detailed technical report with algorithm, results, and analysis

---

## 🧪 Example Execution

**Input Prompt:**
```
Enter values for primary inputs:
Value for N1 (0 or 1): 1
Value for N2 (0 or 1): 0
...
```

**Output:**
```
--- Simulation Output ---
Signal N1: 1
Signal N2: 0
...
Signal N22: 1

--- Boolean Expressions for Output Nets Only ---
N22 = ~((N1 & N8) & N16)
N23 = ~((N7 & N11) & N16)
```

---

## 📊 Technical Concepts

- Logic Gate Evaluation  
- Combinational Circuit Simulation  
- Recursive Boolean Expression Building  
- ISCAS Benchmark Format Parsing  
- Digital Circuit Education & Analysis  

---

## 🎯 Applications

- Educational tool for digital logic courses  
- Gate-level verification and debugging  
- Boolean expression derivation for combinational circuits  
- Preprocessing step for logic synthesis or optimization  


---

## 📩 Contact

For questions, suggestions, or collaboration:  [Urmitkikani1184@gmail.com](mailto:Urmitkikani1184@gmail.com)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) :

---

## 🙌 Acknowledgements

Special thanks to our fellow batchmate [**Neha Golani**](https://github.com/Nehagolani19) for her support throughout the development of this project.  

---

> ⭐ If you find this project useful, consider starring the repo!
