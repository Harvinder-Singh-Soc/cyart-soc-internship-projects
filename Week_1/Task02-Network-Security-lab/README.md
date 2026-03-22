# Task02 – Network Monitoring and Hardening

This repository contains a hands-on lab focused on basic SOC/VAPT activities: capturing and analyzing network traffic, hardening a Linux firewall with iptables, and exploring vulnerability scanning concepts with OpenVAS.

## Lab Components

- **scapy-sniffer**: Python-based packet sniffer built with Scapy to capture and analyze TCP, UDP and ICMP traffic.
- **firewall-iptables**: Firewall configuration using iptables to allow only required services (SSH and HTTP) and block all other inbound traffic.
- **openvas-lab**: Notes and experiments related to installing, configuring and troubleshooting OpenVAS/GVM.
- **report**: Final lab report document that summarizes the environment, methodology, results and key learnings.

## Technologies Used

- Python (Scapy, Matplotlib)
- Linux (Kali / Ubuntu based)
- iptables
- Nmap
- OpenVAS / GVM

## How to Use This Repository

1. Start with the `scapy-sniffer` folder to see the packet capture script and how traffic was analyzed.
2. Move to the `firewall-iptables` folder to review the firewall rules and testing steps using Nmap.
3. Check the `openvas-lab` folder to understand the installation process, common issues and troubleshooting notes.
4. Read the `report` folder (if available) for a complete, written summary of the whole task.

This lab was created to practice real-world style SOC and VAPT workflows: observe traffic, lock down the system, and experiment with vulnerability scanning.
