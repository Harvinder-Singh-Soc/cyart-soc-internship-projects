# Scapy Packet Sniffer

This folder contains a Python script that uses Scapy to capture and analyze live network traffic in a lab environment.

## Features

- Captures packets using Scapy sniffing functions.
- Extracts basic information such as source IP, destination IP, protocol and ports.
- Counts how many packets belong to TCP, UDP and ICMP.
- Generates a simple bar chart to visualize the protocol distribution.

## Files

- `packet_sniffer.py` – Main packet sniffer script.
- `requirements.txt` – Python dependencies (for example: Scapy, Matplotlib).

## How to Run

1. Create and activate a virtual environment (optional but recommended).
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
3. sudo python3 packet_sniffer.py
