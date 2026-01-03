# Snort-IDS-Traffic-Simulator

This project demonstrates network attack simulation and intrusion detection testing using a custom Scapy-based Python script and Snort IDS.

It focuses on generating TCP SYN traffic to emulate port scanning behavior and validating Snort detection rules in a controlled lab environment.

---

## 🔐 Project Overview

- Attacker: Kali Linux  
- Target: Ubuntu VM running Snort IDS  
- Custom Python script generates TCP SYN packets  
- Traffic analysis performed using Wireshark  
- Snort generates alerts for suspicious activity  

---

## 🧪 Features

- Sends a single TCP SYN packet to test basic IDS rules
- Simulates a port scanning attack using multiple SYN packets
- Controlled packet timing to mimic realistic scans
- Triggers Snort threshold-based alerts
- Displays attacker IP, target IP, and destination ports

---

## 🛠 Tools & Technologies

- Kali Linux
- Ubuntu VM
- Python 3
- Scapy
- Snort IDS
- Wireshark

---
## 📡 Wireshark Usage

Wireshark is used to capture and analyze the generated network traffic in real time.  
It helps verify TCP SYN packets sent by the Scapy script and confirms that the traffic
being generated matches the expected attack patterns.

Wireshark analysis is used to:
- Inspect TCP SYN flags
- Validate source and destination IP addresses
- Confirm port scanning behavior
- Correlate packet captures with Snort alerts

### Capture Traffic (Example)
```bash
sudo wireshark

```
or (terminal-based):
```bash
sudo tcpdump -i eth0 tcp
```
## ⚙️ Installation

### 1. Clone or download the repository
(Manual download or GitHub clone)

### 2. Install Python dependencies
```bash
pip3 install -r requirements.txt

```
🚀 Usage
Configure target IP

Edit test_packets.py:
```text
TARGET_IP = "192.168.1.20" # use your own target's ip address here

```
Run the script (root required)
```bash
sudo python3 test_packets.py

```
📊 Expected Output

- SYN packet detected alert
- Potential port scan alert
- Attacker IP → Target IP mapping
- Destination ports listed in alerts

📚 Learning Outcomes

- Intrusion Detection Systems (IDS)
- Snort rule testing and validation
- Network traffic analysis
- Attack simulation using Scapy
- Linux-based security lab setup

 
⚠️ Disclaimer

This project is for educational purposes only.
Do not use this tool on systems you do not own or have explicit permission to test.
