# 🔍 Fault Equivalence and Collapsing for ISCAS-85 c1908 Benchmark

Welcome to the circuit-crushing, fault-busting zone! This project is all about analyzing and optimizing digital circuits by identifying and collapsing **equivalent faults**. We’re working with the `c1908` benchmark circuit from the legendary **ISCAS-85** suite.

---

## 📦 What This Project Does

This project performs the following steps:

1. **Parses the Verilog netlist** of `c1908.v`
2. **Extracts all logic gates, wires, inputs, and outputs**
3. **Generates all possible stuck-at faults** (`SA0`, `SA1`)
4. **Applies fault equivalence rules** to reduce redundant faults
5. **Calculates the fault collapse ratio**
6. **Exports**:
   - Collapsed fault list (`.txt`)
   - Gate type distribution chart (`.png`)
   - Analysis report (`.txt`)

---

## 🧠 Why This Matters

In VLSI testing, **fault collapsing** is a key optimization technique. It reduces the number of test patterns needed during manufacturing by eliminating redundant faults — saving time, cost, and power.

---

## 🧰 Tech Stack

- 🐍 Python 3.x
- 🧮 `re` for parsing
- 📊 `matplotlib` for visualizations
- 🧠 Basic logic for gate-level fault equivalence

---

## 📂 Files Generated

| File                         | Description                                    |
|-----------------------------|------------------------------------------------|
| `c1908_fault_report.txt`    | Summary report of fault collapsing             |
| `c1908_collapsed_faults.txt`| List of reduced faults after collapsing        |
| `c1908_gate_distribution.png` | Pie chart of gate type distribution          |

---

## 🚀 How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/c1908-fault-collapsing.git
   cd c1908-fault-collapsing
    
2. Make sure you have Python and matplotlib installed:
  ```bash
  pip install matplotlib
  ```

3. Drop your `c1908.v` Verilog file in the same directory.

4. ```bash
   python proj.py
   ```
