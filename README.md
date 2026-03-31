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

# CyArt SOC Internship – Hands-on Projects

This repository contains my week-by-week work from the CyArt SOC Analyst Internship.  
Each project focuses on real-world SOC skills: network design, offensive testing in a lab, traffic analysis, SIEM, and clear documentation.

---

## Repository Structure

- `Week_1/` – Foundations (Linux, networking, basic security tooling)
- `Week_2/` – Network design, HTTPS analysis, SOC networking & SIEM lab
- Each week/day includes:
  - A detailed PDF report following CyArt’s documentation format [file:128]
  - Screenshots and diagrams
  - Configs, scripts, and notes used in the lab [file:127]

---

## Week 2 – Key Projects

### Day 04 – Secure Network Design, Metasploit Exploitation & HTTPS Analysis

**Goal:** Connect secure network architecture, penetration testing, and encrypted traffic analysis into one workflow. [file:127]

What this project covers:

- Designed a secure small-office topology:
  - DMZ for public-facing services
  - Internal employee VLAN
  - Guest VLAN with Internet-only access
  - Clear firewall rules between zones
- Built a VirtualBox lab:
  - Kali Linux (attacker)
  - Metasploitable 2 (vulnerable target)
- Performed a structured penetration test:
  - Service enumeration with `db_nmap` inside Metasploit
  - Identified vulnerable `vsftpd 2.3.4` on FTP port 21
  - Exploited the vsftpd backdoor module and obtained a Meterpreter session and root shell
- Analysed encrypted HTTPS traffic:
  - Captured real HTTPS traffic in Wireshark
  - Wrote `traffic_analyzer.py` using PyShark + Matplotlib
  - Parsed packet metadata (IPs, sizes, counts) and generated a packet size distribution histogram [file:127]

**Artifacts:**

- Report: `Week_2/Day04/day04_report.pdf`  
- Scripts: `Week_2/Day04/traffic_analyzer.py` (and related files)  
- Screenshots: Wireshark capture, Metasploit console, packet size histogram

---

### Day 05 – SOC Networking & SIEM Lab (SSH Brute-Force Detection)

**Goal:** Build a small SOC lab, generate real attack traffic, and detect it in a SIEM.

Lab environment:

- **Network:**
  - Small office subnet with `/27` planning
  - Separate VirtualBox host-only lab network
- **Virtual machines:**
  - Kali – attacker (Hydra, Nmap, Wireshark)
  - Linux Mint – victim (SSH target + Elastic Agent)
  - ELK server – SIEM backend (Elasticsearch + Kibana + Fleet)

What this project covers:

- Designed and documented the lab topology and IP plan
- Captured normal and “broken” traffic with Wireshark to practice troubleshooting:
  - Misconfigured routes / unreachable network
  - Fixes validated with ICMP pings
- Deployed ELK stack and Fleet:
  - Collected system and auth logs from the Mint victim
  - Verified SSH events in Kibana Discover
- Simulated an SSH brute-force attack:
  - Used Hydra from Kali against SSH on the Mint host
  - Captured SSH traffic in Wireshark
  - Built Kibana visualizations to:
    - Show spikes in failed logins over time
    - Highlight attacker IPs and usernames
    - Confirm that no successful login occurred from the attacker IP

**Artifacts:**

- Folder: `Week_2/SOC-Networking-SIEM-Lab/`
- Report: `Week_2/SOC-Networking-SIEM-Lab/report/Day05_report.pdf`
- Screenshots:  
  - Subnet topology and lab diagram  
  - Wireshark protocol hierarchy and I/O graph  
  - Hydra brute-force terminal output  
  - Fleet Agents page  
  - Kibana Discover and dashboards

---

## Skills Demonstrated

**Networking & Infrastructure**

- IPv4 subnetting, VLANs, DMZ design and segmentation
- VirtualBox networking (NAT + host-only)
- Network troubleshooting with `ip`, `ping`, routes, and Wireshark [file:127]

**Offensive Security (in a controlled lab)**

- Nmap and Metasploit for reconnaissance and exploitation
- Exploiting `vsftpd 2.3.4` on Metasploitable 2 to gain a root shell [file:127]

**Blue Team / SOC**

- SIEM setup with ELK (Elasticsearch + Kibana + Fleet)
- Log collection (system + auth logs) from Linux hosts
- Detecting SSH brute-force activity using log fields and visualizations
- Working with encrypted traffic via metadata (HTTPS packet analysis) [file:127]

**Documentation & Reporting**

- Professional reports that follow CyArt documentation standards:
  - Clear structure, visuals, captions, and explanations
  - Focus on making the lab reproducible and understandable [file:128]

---

## How to Use This Repository

- Browse the `Week_x` folders in order.
- For each project/day:
  - Start with the PDF report to understand the scenario and objectives.
  - Open the lab folder (screenshots, scripts, configs) to replicate or extend the work.
- This repo is built to show **practical SOC workflows**, not just tool screenshots:
  - Design → Attack → Capture → Detect → Document.
