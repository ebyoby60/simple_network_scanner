# 🔍 Simple Network Scanner & HTTPS SNI Logger

A two-phase cybersecurity project that scans a local network for connected devices and logs HTTPS packets by extracting Server Name Indication (SNI) values from TLS handshakes.

 📁 Project Folder Structure


---

## 🧠 Project Overview

This project is structured in **two phases**:

### 🔹 Phase 1: Device Scanner (Managed Mode)
- Uses ARP requests to identify devices on the local network.
- Implemented using `Scapy`.

### 🔹 Phase 2: HTTPS SNI Sniffer (Monitor Mode)
- Captures HTTPS traffic using `PyShark`.
- Extracts SNI domains from TLS Client Hello packets.
- Requires monitor mode interface (e.g., `wlan0`).

---

## 🎯 Project Objectives

- Detect all connected devices on a subnet.
- Log HTTPS domains visited (via SNI field).
- Summarize domain frequencies for network insights.
- Demonstrate use of Python and packet-level inspection.

-🏆 Achievements

✅ ARP-based device detection  
✅ SNI domain extraction from HTTPS  
✅ CSV and TXT log conversion  
✅ Frequency summary of SNI data  
✅ Modular CLI-based design  
✅ Cross-platform support (Linux and Windows transfer)

⚙️ Tools & Environment

- **OS**: Kali Linux (development), Windows (transfer/log analysis)
- **Python**: 3.x (inside virtual environment)
- **Libraries**: `scapy`, `pyshark`
- **Interfaces**: `wlan0` (monitor mode)
- **Tools**: `Wireshark`, `tshark`, `ip`, `iw`

 📦 Installation

Install Python dependencies:

```bash
pip install -r requirements.txt


---

## 🧠 Project Overview

This project is structured in **two phases**:

### 🔹 Phase 1: Device Scanner (Managed Mode)
- Uses ARP requests to identify devices on the local network.
- Implemented using `Scapy`.

### 🔹 Phase 2: HTTPS SNI Sniffer (Monitor Mode)
- Captures HTTPS traffic using `PyShark`.
- Extracts SNI domains from TLS Client Hello packets.
- Requires monitor mode interface (e.g., `wlan0`).

---

## 🎯 Project Objectives

- Detect all connected devices on a subnet.
- Log HTTPS domains visited (via SNI field).
- Summarize domain frequencies for network insights.
- Demonstrate use of Python and packet-level inspection.

---

## 🏆 Achievements

✅ ARP-based device detection  
✅ SNI domain extraction from HTTPS  
✅ CSV and TXT log conversion  
✅ Frequency summary of SNI data  
✅ Modular CLI-based design  
✅ Cross-platform support (Linux and Windows transfer)

 ⚙️ Tools & Environment

- **OS**: Kali Linux (development), Windows (transfer/log analysis)
- **Python**: 3.x (inside virtual environment)
- **Libraries**: `scapy`, `pyshark`
- **Interfaces**: `wlan0` (monitor mode)
- **Tools**: `Wireshark`, `tshark`, `ip`, `iw`

 📦 Installation

Install Python dependencies:

bash
pip install -r requirements.txt

Contents of requirements.txt:
scapy
pyshark

You must also install tshark (Wireshark CLI):
sudo apt install tshark

Usage
Scan Devices (Phase 1)
sudo python scanner_sni_logger.py --scan

Capture HTTPS SNI (Phase 2)
sudo python scanner_sni_logger.py --sniff --interface wlan0

Run Both Together
sudo python scanner_sni_logger.py --both --interface wlan0

Example Output
Connected Devices:

IP: 192.168.43.1, MAC: 10:44:00:56:6b:8c
IP: 192.168.43.241, MAC: 30:3a:64:98:57:15

SNI Domains:

[+] SNI found: ssl.gstatic.com
[+] SNI found: chatgpt.com

 Log Analysis Scripts

convert_log_to_csv.py: Converts text log to CSV format.
count_sni_frequencies.py: Analyzes SNI domain frequency.
utils.py: Ensures logs/ directory exists.

Challenges & Fixes
Challenge	Solution
Interface not in monitor mode	Used ip and iw to switch mode
ModuleNotFoundError	Installed in virtual environment
No SNI captured	Corrected filters, checked interface
Permission denied	Used chmod or ran with sudo

🛡️ Ethical Use Notice
This tool is intended for educational purposes and authorized environments only. Unauthorized packet sniffing may violate privacy laws and institutional policies.

📌 Recommendations for Demonstration
Live scan and sniff demo

Explain script structure and CLI usage

Showcase .csv and .txt logs

Highlight real-world applications (e.g., threat intel, monitoring)

🌱 Future Enhancements
Map IP addresses to domain names

Add blacklist alert for malicious SNI domains

Include GUI for real-time visualization

Timestamp SNI logs for better traceability

👩‍💻 Author
Mbakpobe Adaeze
Cybersecurity Researcher & Developer
📧 adaezeoby37@gmail.com
🔗 GitHub: ebyoby60

 License
MIT License – Free to use and modify with attribution.
</details>




