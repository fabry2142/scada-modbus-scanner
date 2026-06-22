# scada-modbus-scanner
# SCADA Modbus TCP Security Scanner (Safe Proof-of-Concept)

A lightweight industrial reconnaissance and vulnerability assessment tool written in Python, engineered to audit SCADA/OT environments running the Modbus TCP protocol.

## 🛡️ Responsible Use & Safe-PoC Design
To strictly prevent the malicious use or weaponization of this repository, this tool has been engineered as a **Safe Proof-of-Concept (PoC)**:
* **No Data Extraction:** The code is strictly limited to connection handshakes. It **does not read, write, or modify** PLC registers, memory maps, or industrial telemetry.
* **Immediate Disconnection:** Once an unauthenticated port `502` is identified, the script aborts the session immediately to guarantee zero operational impact on the target node.
* **Non-Invasive Diagnostics:** Designed exclusively to help OT Security Engineers verify compliance and network segregation without risking system downtime.

## 🚀 Installation & Quick Start
```bash
pip install pymodbus
python modbus_scanner.py <TARGET_INDUSTRIAL_IP>
