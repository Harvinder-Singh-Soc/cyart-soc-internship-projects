# Day 03 – Network Security Monitoring and Analysis (CyArt)

This lab demonstrates how to monitor and detect simple port-scan style activity using **Wireshark**, **Snort 3**, and **Scapy** on a Kali Linux virtual machine.

The goal is to generate SYN packets with Scapy, observe them in Wireshark, and detect them using custom Snort rules.

---

## Lab Environment

- **OS:** Kali Linux (VirtualBox, NAT)
- **Interface:** `eth0` (e.g. `10.0.2.15`)
- **Tools:**
  - Wireshark – packet capture and analysis
  - Snort++ 3.11.1.0 – IDS with Lua configuration
  - Python 3 + Scapy – packet generation

Folder layout (suggested):

```text
Day03-Network-Monitoring/
├── test_packets.py
├── configs/
│   ├── snort.lua         # sanitized snippet / example
│   └── local.rules       # custom rules
├── captures/
│   └── capture.pcap
├── screenshots/
│   ├── wireshark_*.png
│   └── snort_*.png
└── report/
    └── Day03_Network_Monitoring_Report_CyArt.pdf
