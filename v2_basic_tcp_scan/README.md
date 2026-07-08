# 🔍 PyPort Scout - v2.0 (Enhanced TCP Port Scanner)

PyPort Scout v2.0 is the second release of this Python-based TCP port scanner project.

Building on the foundation created in **v1 (Basic TCP Port Scanner)**, this version introduces improved usability, better input handling, and customizable scanning options.

The goal of v2 is to move closer towards a more flexible reconnaissance tool while keeping the code simple, readable, and beginner-friendly.

---

# ⚠️ Disclaimer

This tool is intended for educational purposes and authorized security testing only.

Only scan systems that you own or have explicit permission to assess.

Unauthorized scanning of networks or systems may violate laws or security policies.

---

# 📌 Overview

Version 2 improves the original scanner by allowing users to define their own scan range instead of relying on a fixed port range.

New improvements include:

* Custom starting port selection
* Custom ending port selection
* Improved error handling
* Target validation
* Version identification
* Cleaner scan summaries
* Improved code structure

---

# 🚀 New Features Compared To v1

| Feature              | v1 | v2 |
| -------------------- | -- | -- |
| TCP Connect Scanning | ✅  | ✅  |
| Detect Open Ports    | ✅  | ✅  |
| Count Closed Ports   | ✅  | ✅  |
| Custom Port Range    | ❌  | ✅  |
| Input Validation     | ❌  | ✅  |
| Version Display      | ❌  | ✅  |
| Improved Reporting   | ❌  | ✅  |

---

# ⚙️ How To Run

## Requirements

PyPort Scout requires:

* Python 3.x
* No external libraries

The scanner uses built-in Python modules:

```python
socket
datetime
```

---

## Running The Scanner

Navigate to the v2 directory:

```bash
cd v2_enhanced_tcp_scan
```

Run:

```bash
python scanner.py
```

---

# 🖥️ Scanner Workflow

When started, the scanner will ask for:

### 1. Target

Enter either:

* IP address

Example:

```text
192.168.1.10
```

or:

* Domain name

Example:

```text
example.com
```

---

### 2. Starting Port

Enter the first port you want to scan.

Example:

```text
Starting port: 1
```

---

### 3. Ending Port

Enter the last port you want to scan.

Example:

```text
Ending port: 100
```

The scanner will then check every TCP port between the selected range.

---

# 📊 Example Scan

Example session:

```text
========================================
PyPort Scout v2.0
========================================

Enter target IP/domain: example.com

Starting port: 1
Ending port: 100


Target: example.com
Port Range: 1-100

Resolved IP: xxx.xxx.xxx.xxx


[OPEN] Port 80


========== Scan Summary ==========

Ports scanned: 100

Open ports: 1

Closed ports: 99

Open ports found:
- 80

Scan completed.
```

---

# 🧠 How The Scanner Works

## 1. Host Resolution

The scanner converts a hostname into an IP address using Python's socket library.

Example:

```python
socket.gethostbyname(host)
```

This allows users to scan either domains or direct IP addresses.

---

## 2. TCP Connection Test

Each selected port is tested using:

```python
socket.connect_ex((ip, port))
```

The result determines the port status:

* `0` → Port is open
* Non-zero → Port is closed or unreachable

---

## 3. Port Range Scanning

Unlike v1, where the scan range was fixed, v2 allows the user to decide the range.

Example:

```text
1-100
```

The scanner checks:

```text
Port 1
Port 2
Port 3
...
Port 100
```

---

# 📋 Scan Summary Explanation

At the end of the scan, the tool displays:

| Result           | Meaning                               |
| ---------------- | ------------------------------------- |
| Ports scanned    | Total number of ports tested          |
| Open ports       | Number of ports accepting connections |
| Closed ports     | Number of ports that did not respond  |
| Open ports found | List of discovered open ports         |

---

# ⚠️ Current Limitations

Although v2 improves flexibility, it is still a learning-focused scanner.

Current limitations:

* Single-threaded scanning
* No service detection
* No banner grabbing
* No export reports
* No command-line arguments
* TCP scanning only

---

# 🚀 Future Improvements (v3 Roadmap)

Planned improvements:

* 🔍 Service/banner detection
* ⚡ Multi-threaded scanning
* 📁 JSON/TXT reporting
* 🖥 Command-line arguments
* 📊 Scan progress display
* 🧠 Scan profiles (quick/full scans)
* 🎨 Improved terminal interface

---

# 📚 Learning Objectives

PyPort Scout v2 demonstrates:

* Python socket programming
* TCP communication
* Port enumeration concepts
* Input validation
* Basic reconnaissance workflows
* Progressive software development

---

# 📄 Version Information

Project:

```text
PyPort Scout
```

Version:

```text
v2.0
```

Status:

```text
Enhanced Scanner Release
```
