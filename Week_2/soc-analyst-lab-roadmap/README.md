# SOC Analyst Learning Roadmap – Lab Portfolio

This repository contains my hands-on practical work for a **SOC Learning Roadmap** sprint. It demonstrates core Tier 1 SOC analyst skills including log analysis, SIEM configuration, detection engineering, and incident response using a self-built virtual lab.

## 📁 Contents

| Folder | Description |
|--------|-------------|
| `/report` | Final lab report (PDF) following professional documentation standards. |
| `/screenshots` | 35+ original screenshots showing tool usage and key findings. |
| `/scripts` | Custom rules and commands used during the lab. |

## 🛠️ Lab Environment

| Machine | IP Address | Role |
|---------|------------|------|
| Windows 10 Client | 192.168.56.137 | Victim Endpoint |
| ELK Server (Linux Mint) | 192.168.10.129 | Elasticsearch & Kibana |
| Wazuh Server | 192.168.56.131 | XDR / Additional SIEM |
| Snort IDS (Ubuntu) | 192.168.56.132 | Intrusion Detection |
| Kali Linux | 192.168.56.133 | Attacker Machine |
| Metasploitable2 | 192.168.56.136 | Vulnerability Scan Target |

## ✅ Tasks Completed

- **P1 – Log Analysis:** Brute-force detection via Windows Event ID 4625 & browser forensics attempt.
- **P2 – Incident Documentation:** Structured incident logging & firewall containment.
- **P3 – Monitoring Dashboards:** Kibana visualizations for failed logons.
- **P4 – Alert Rules:** Custom detection rules in Elastic SIEM and Wazuh.
- **T4 – Security Tools:** Snort IDS rule & alerts, Nessus vulnerability scan with manual validation, Osquery endpoint monitoring.

## 🔍 Key Findings

- Multiple failed network logons (Event ID 4625, Logon Type 8) targeting non‑existent users.
- Nessus identified critical backdoors (Bind Shell, UnrealIRCd) – manually validated with Nmap and Netcat.
- Snort successfully triggered alerts for a test malicious domain.

## 🔗 References

- MITRE ATT&CK
- NIST SP 800‑61
- Elastic & Wazuh Documentation

---
*This project was completed as part of a self‑directed SOC training sprint.*