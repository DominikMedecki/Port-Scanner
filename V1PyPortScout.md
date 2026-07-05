# 🔍 PyPort Scout - v1 (Basic TCP Port Scanner)

A simple Python-based TCP port scanner inspired by tools like Nmap.  
This is the **first version (v1)** in a growing cybersecurity/red-team learning project.

⚠️ **Disclaimer:**  
This tool is intended for educational use and authorized testing only.  
Do not scan systems you do not own or have permission to test.

---

## 📌 Overview

This scanner checks a target host (IP or domain) for open TCP ports within a defined range.

Instead of displaying every closed port, it focuses on:
- Open ports (services of interest)
- A summary of closed ports

This makes the output cleaner and more useful for reconnaissance-style scanning.

---

## ⚙️ How It Works

### 1. Target Resolution
The scanner first takes a user input:

- IP address (e.g. `192.168.1.1`)
- or domain name (e.g. `example.com`)

It then resolves the domain to an IP address using Python’s `socket` library.

---

### 2. Port Scanning Logic
For each port in the scan range:

- A TCP connection attempt is made using `socket.connect_ex()`
- If the connection succeeds → the port is **OPEN**
- If it fails → the port is counted as **CLOSED**

No services are exploited or interacted with — only connection checks are performed.

---

### 3. Output Handling

Instead of printing every result, the scanner:

- Prints each **open port immediately**
- Tracks the number of closed ports internally
- Displays a final summary at the end

Example output:
[OPEN] Port 22
[OPEN] Port 80

--- Scan Complete ---

Open ports found:

22
80

Closed ports: 1022

---

## 🧠 Technical Breakdown

### Libraries used:
- `socket` → handles TCP connections
- `datetime` → timestamps scan start time

### Core function:
```python
socket.connect_ex((ip, port))

This returns:
0 → port is open

non-zero → port is closed or unreachable
📊 Default Scan Range

The scanner checks:

Ports 1 - 1024

This covers common service ports such as:

SSH (22)
HTTP (80)
HTTPS (443)
FTP (21)
DNS (53)

🚀 Future Improvements (v2+ roadmap)

This project is designed to evolve into a full Nmap-style tool.

Planned upgrades:

🔍 Service/banner detection
⚡ Multi-threaded scanning (faster performance)
📁 JSON/TXT scan reports
🎯 Custom port range input
🧠 Scan profiles (quick/full / stealth mode)
