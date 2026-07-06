# 🔍 PyPort Scout - v1 (Basic TCP Port Scanner)

Version 1 of **PyPort Scout** is a lightweight TCP connect port scanner written in Python. It provides the foundation for the project by implementing the core principles of TCP port scanning using Python's built-in networking libraries.

This version focuses on simplicity and readability, making it an excellent starting point for learning how port scanners work before introducing more advanced functionality in later releases.

> **Disclaimer**
>
> This tool is intended for educational purposes and authorized security testing only. Only scan systems that you own or have explicit permission to assess.

---

# 📌 Features

* Scan a target using an IP address or hostname
* Resolve hostnames to IP addresses
* Perform TCP connect scans
* Display open ports only
* Count and summarize closed ports
* Timestamp each scan
* Lightweight with no third-party dependencies

---

# 📸 Example Output

> **Screenshot coming soon**

*Replace this section with a screenshot of the scanner running after your first release.*

```
+--------------------------------------------------+
|                 Screenshot Placeholder           |
|                                                  |
|        (Terminal output will be added here)      |
|                                                  |
+--------------------------------------------------+
```

---

# ⚙️ How It Works

## 1. Target Resolution

The scanner prompts the user to enter either:

* An IPv4 address (e.g. `192.168.1.1`)
* A hostname or domain (e.g. `example.com`)

If a hostname is provided, Python's `socket.gethostbyname()` function resolves it to an IPv4 address before scanning begins.

---

## 2. TCP Port Scanning

The scanner loops through a predefined range of TCP ports.

For each port it:

1. Creates a TCP socket.
2. Attempts to establish a connection.
3. Determines whether the port is open or closed.
4. Closes the socket before moving to the next port.

Version 1 uses a **TCP Connect Scan**, one of the simplest and most reliable techniques for determining whether a TCP port is accepting connections.

---

## 3. Output Handling

Instead of printing every closed port, Version 1 focuses on the information that matters most.

The scanner:

* Displays each open port as it is discovered.
* Counts closed ports internally.
* Prints a summary once the scan has completed.

Example output:

```text
[OPEN] Port 22
[OPEN] Port 80

--- Scan Complete ---

Open ports found:
  - 22
  - 80

Closed ports: 1022
```

---

# 🧠 Technical Breakdown

## Python Libraries

| Library    | Purpose                          |
| ---------- | -------------------------------- |
| `socket`   | TCP networking and port scanning |
| `datetime` | Displays the scan start time     |

---

## Core Function

The scanner determines whether a port is open using:

```python
socket.connect_ex((ip, port))
```

Return values:

* `0` → Connection successful (port is open)
* Non-zero value → Connection failed (port is closed or unreachable)

This method allows the scanner to determine the state of each TCP port without generating unnecessary output.

---

# 📊 Default Scan Range

Version 1 scans TCP ports:

```text
1 - 1024
```

These ports include many well-known services, such as:

| Port | Common Service |
| ---: | -------------- |
|   21 | FTP            |
|   22 | SSH            |
|   53 | DNS            |
|   80 | HTTP           |
|  443 | HTTPS          |

---

# ⚠️ Current Limitations

Version 1 is intentionally simple.

Current limitations include:

* Single-threaded scanning
* Fixed scan range (1–1024)
* TCP scans only
* No service or banner detection
* No report generation
* No command-line arguments
* No scan profiles

These limitations will be addressed in future versions.

---

# 🚀 Planned Improvements

The following features are planned for Version 2 and beyond:

* Service/banner detection
* User-defined port ranges
* JSON and TXT report generation
* Command-line interface (CLI)
* Multi-threaded scanning
* Scan profiles
* Improved performance
* Better error handling
* Additional output formatting

---

# 📚 Learning Objectives

Version 1 demonstrates several fundamental networking concepts:

* Socket programming in Python
* TCP connection establishment
* Hostname resolution
* Sequential port scanning
* Basic reconnaissance techniques
* Simple terminal-based reporting

---

# 📄 Version Information

**Project:** PyPort Scout

**Version:** 1.0.0

**Status:** Stable

This release serves as the foundation for all future versions of the project.

