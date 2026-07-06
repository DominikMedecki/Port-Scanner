# 🔍 PyPort Scout

A Python-based TCP port scanner built as a progressive cybersecurity learning project.

Rather than producing a single finished tool, PyPort Scout is being developed in stages, with each version introducing new features and improvements. The goal is to demonstrate the evolution of a port scanner from a simple TCP connect scanner into a more capable reconnaissance utility inspired by industry-standard tools such as Nmap.

> **Disclaimer**
>
> This project is intended for educational purposes and authorized security testing only. Only scan systems that you own or have explicit permission to assess.

---

## 📖 Project Overview

PyPort Scout demonstrates the fundamentals of TCP port scanning using Python's networking libraries. As the project grows, new versions will introduce additional functionality while maintaining previous versions as reference implementations.

Current capabilities include:

* TCP connect scanning
* Hostname to IP resolution
* Detection of open TCP ports
* Summary of closed ports
* Clean terminal output

Future versions will expand these capabilities with additional scanning and reporting features.

---

## 📂 Repository Structure

```text
PyPort-Scout/
│
├── README.md
├── CHANGELOG.md
│
├── v1_basic_tcp_scan/
├── v2_enhanced_scan/
├── v3_threaded_scan/
└── screenshots/
```

Each version represents a milestone in the development of the scanner.

---

## 🚀 Version Roadmap

| Version   | Status         | Description                                                           |
| --------- | -------------- | --------------------------------------------------------------------- |
| ✅ v1      | Complete       | Basic TCP connect scanner                                             |
| 🚧 v2     | In Development | Service detection, configurable scan ranges, improved reporting       |
| 📅 v3     | Planned        | Multi-threaded scanning and performance improvements                  |
| 📅 Future | Planned        | Additional scanning techniques, reporting, and usability improvements |

---

## ✨ Current Features

* Scan a target IP address or hostname
* Resolve domain names to IP addresses
* Scan TCP ports
* Display open ports only
* Count closed ports
* Timestamp scan execution

---

## 🛠 Technologies Used

* Python 3
* socket
* datetime

No third-party dependencies are required for Version 1.

---

## 📚 Documentation

Detailed documentation for each version can be found inside its respective directory.

* `v1_basic_tcp_scan/README.md`
* `v2_enhanced_scan/README.md` *(coming soon)*
* `v3_threaded_scan/README.md` *(coming soon)*

---

## 📈 Project Goals

This repository is intended to demonstrate:

* Python programming
* Socket programming fundamentals
* TCP networking concepts
* Reconnaissance techniques
* Progressive software development
* Version-controlled feature evolution

---

## ⚖️ Legal Notice

This software is provided for educational and defensive security purposes only.

The author is not responsible for any misuse of this software. Users are responsible for ensuring they have proper authorization before scanning any systems or networks.

---

## 📄 License

This project will be released under the MIT License.
