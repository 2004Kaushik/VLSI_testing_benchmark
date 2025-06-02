import re
import matplotlib.pyplot as plt
from collections import defaultdict

# === [PART 1] Read and parse Verilog file ===
with open("c1908.v", "r") as f:
    verilog_code = f.read()

verilog_code = re.sub(r"//.*", "", verilog_code)
verilog_code = verilog_code.replace("\n", " ")

def extract_signals(matches):
    signals = []
    for match in matches:
        parts = match.split(',')
        for part in parts:
            clean = part.strip()
            if clean:
                signals.append(clean)
    return signals

inputs = extract_signals(re.findall(r"\binput\s+(.*?);", verilog_code))
outputs = extract_signals(re.findall(r"\boutput\s+(.*?);", verilog_code))
wires = extract_signals(re.findall(r"\bwire\s+(.*?);", verilog_code))

gate_re = re.compile(r"\b(and|or|nand|nor|xor|xnor|not)\s+(\w+)\s*\((.*?)\);")
gates = []
gate_counts = defaultdict(int)

for match in gate_re.findall(verilog_code):
    gtype, name, signals = match
    signal_list = [s.strip() for s in signals.split(',')]
    gates.append({
        "type": gtype,
        "name": name,
        "output": signal_list[0],
        "inputs": signal_list[1:]
    })
    gate_counts[gtype] += 1

# === [PART 2] Fault generation + collapsing ===
all_faults = [(w, 'SA0') for w in wires] + [(w, 'SA1') for w in wires]

collapsed_faults = set()

for gate in gates:
    gtype = gate["type"]
    inputs = gate["inputs"]
    output = gate["output"]

    if gtype == "not":
        collapsed_faults.add((inputs[0], 'SA0'))
        collapsed_faults.add((output, 'SA0'))
    elif gtype in ["and", "nand"]:
        collapsed_faults.add((output, 'SA0'))
        for i in inputs:
            collapsed_faults.add((i, 'SA1'))
    elif gtype in ["or", "nor"]:
        collapsed_faults.add((output, 'SA1'))
        for i in inputs:
            collapsed_faults.add((i, 'SA0'))
    elif gtype in ["xor", "xnor"]:
        for i in inputs:
            collapsed_faults.add((i, 'SA0'))
            collapsed_faults.add((i, 'SA1'))
        collapsed_faults.add((output, 'SA0'))
        collapsed_faults.add((output, 'SA1'))
    else:
        for i in inputs:
            collapsed_faults.add((i, 'SA0'))
            collapsed_faults.add((i, 'SA1'))
        collapsed_faults.add((output, 'SA0'))
        collapsed_faults.add((output, 'SA1'))

# === [PART 3] Export collapsed faults to file ===
with open("c1908_collapsed_faults.txt", "w") as f:
    for fault in sorted(collapsed_faults):
        f.write(f"{fault[0]} {fault[1]}\n")

# === [PART 4] Visualize gate distribution ===
plt.figure(figsize=(6, 6))
plt.title("Gate Type Distribution in c1908")
plt.pie(gate_counts.values(), labels=gate_counts.keys(), autopct='%1.1f%%')
plt.savefig("c1908_gate_distribution.png")
plt.close()

# === [PART 5] Generate summary report ===
original_faults = len(all_faults)
collapsed = len(collapsed_faults)
collapse_ratio = round(collapsed / original_faults, 4)

report = f"""
ISCAS-85 Benchmark: c1908 Fault Equivalence Analysis Report
-----------------------------------------------------------
Primary Inputs: {len(inputs)} ({', '.join(inputs[:5])}...)
Primary Outputs: {len(outputs)} ({', '.join(outputs[:5])}...)
Total Internal Wires: {len(wires)}
Total Gates: {len(gates)}

Fault Analysis:
   - Total Faults Before Collapsing: {original_faults}
   - Total Faults After Collapsing: {collapsed}
   - Collapse Ratio: {collapse_ratio}

Gate Type Distribution:
"""
for gtype, count in gate_counts.items():
    report += f"   - {gtype.upper():<5}: {count}\n"

with open("c1908_fault_report.txt", "w", encoding="utf-8") as f:
    f.write(report)

print("All tasks complete!")
print("Files created:")
print(" - c1908_collapsed_faults.txt")
print(" - c1908_fault_report.txt")
print(" - c1908_gate_distribution.png")
