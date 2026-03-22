
***

## 3. `firewall-iptables/README.md`

```markdown
# Firewall Hardening with iptables

This folder contains the firewall configuration used to restrict inbound traffic on a Linux host using iptables.

## Goal

Allow only required services (SSH on port 22 and HTTP on port 80) and block all other inbound connections.

## Files

- `firewall_rules.sh` – Script containing the iptables rules.
- `lab_topology.png` (optional) – Diagram of the virtual lab network showing attacker, target and firewall.

## Applied Rules (High Level)

- Flush existing iptables rules.
- Set default policy for the INPUT chain to DROP.
- Allow established and related connections.
- Allow SSH (port 22) from the lab network.
- Allow HTTP (port 80) from the lab network.
- Drop all other inbound traffic.

## How to Apply the Rules

1. Make the script executable:

   ```bash
   chmod +x firewall_rules.sh
