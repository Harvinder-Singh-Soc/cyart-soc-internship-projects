## About Me

Hi, I’m **Harvinder Singh**, a cybersecurity trainee focusing on **SOC operations**.

I enjoy building small, realistic labs in VirtualBox and then breaking and monitoring them with
tools like **Kali Linux, Metasploitable, Metasploit, Nmap, Wireshark, Snort 3 and Python**.
Most of my work here comes from the **CyArt SOC Internship**, where each task ends with a
proper PDF report, screenshots and (whenever possible) reusable scripts.

Right now I’m especially interested in:

- Turning raw packet captures into useful insights with Python
- Combining attacker workflows (recon → exploit → post‑ex) with defender workflows (logs, IDS, traffic analysis)
- Building a portfolio that shows real hands‑on skills, not just theory

# CyArt SOC Internship – Projects

This repository contains all my hands‑on work from the **CyArt SOC Internship**.  
Each folder represents a task or day where I built and documented a small security lab
using tools like Kali Linux, Metasploitable, Wireshark, Snort, Metasploit and Python.
## Completed Tasks

| Week | Task / Day | Description | Report |
|------|-----------|-------------|--------|
| 1    | Task 01   | \<1–2 line summary\> | [task01_report.pdf](task01_report.pdf) |
| 1    | Task 02   | \<1–2 line summary\> | [task02_report.pdf](task02_report.pdf) |
| 1    | Day 03 – Network Security Monitoring and Analysis | Wireshark + Snort 3 + Scapy based SYN scan detection | [Day03_Network_Monitoring_Report_CyArt.pdf](Day03_Network_Monitoring_Report_CyArt.pdf) |
| 2    | Day 04 – Secure Network Design, Metasploit Pentest and HTTPS Analysis | DMZ/VLAN design, vsftpd exploit, HTTPS metadata analysis using Python | [day04_report.pdf](day04_report.pdf) |
## Highlight – Day 04 Traffic Analyzer (Python)

In `day04/traffic_analyzer.py` I wrote a small analysis script that:

- Reads an HTTPS capture (`day04_https_capture.pcapng`) using **PyShark**
- Extracts source/destination IPs and packet lengths
- Prints stats (1542 packets in my lab, 74–5158 bytes)
- Generates a clean packet size distribution chart

This is a good example of using Python for security automation and report‑ready visualisation.
