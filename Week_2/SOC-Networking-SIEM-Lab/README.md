# SOC Lab – Networking, Traffic Analysis, and SIEM (Day 05)

Hands-on SOC project combining subnet design, Wireshark analysis, protocol troubleshooting, and ELK-based SIEM monitoring for an SSH brute-force attack.

## Lab Topology & IP Plan

The lab uses two VirtualBox networks:
- **NAT adapter** on some VMs for Internet access.
- **Host-only network** for isolated attack/monitoring traffic.

### Virtual Machines

- **ELK-SERVER**
  - Role: SIEM backend (Elasticsearch + Kibana + Fleet Server)
  - OS: Linux Mint
  - NICs:
    - Host-only: `192.168.10.129`
  - Lab subnet: `192.168.10.128/27`

- **Kali (Attacker)**
  - Role: Offensive box (Hydra, Nmap, Wireshark)
  - NICs:
    - NAT: Internet access (DHCP from VirtualBox)
    - Host-only: `192.168.10.131`
  - Used for: SSH brute-force, pings, packet captures.

- **mint-victim (Linux Mint)**
  - Role: SSH target + log source for SIEM
  - NICs:
    - NAT: optional Internet updates
    - Host-only: `192.168.10.132`
  - Services: OpenSSH on TCP 22, Elastic Agent (System + System auth).

### Host-only Lab Subnet

- Network: `192.168.10.128/27`
- Mask: `255.255.255.224`
- Used IPs:
  - `192.168.10.129` – ELK-SERVER
  - `192.168.10.131` – Kali
  - `192.168.10.132` – mint-victim

## 1. Small Office Subnet Design

- Designed a /27 subnet: `192.168.1.0/27` (30 usable hosts) for a 20-device office.
- Built the LAN in Cisco Packet Tracer with 20 PCs connected to a central switch.
- Validated connectivity using ICMP ping between hosts (0% packet loss).

**Artifacts:**

- `report/Day05_report.pdf` – full writeup (Section 3).
- `screenshots/subnet_topology.png`
- `screenshots/pt_ping_192-168-1-10.png`

## 2. Traffic Capture and Troubleshooting

- Captured normal host-only traffic with Wireshark and analysed:
  - Protocol Hierarchy (IPv4, TCP/UDP, DNS, ARP).
  - I/O Graphs to spot short traffic spikes.
- Broke Kali routing on purpose → `Network is unreachable` + no ICMP packets on wire.
- Fixed routes/interfaces and confirmed successful pings to `192.168.10.131`, `8.8.8.8`, and `google.com`.

**Artifacts:**

- `screenshots/wireshark_protocol_hierarchy.png`
- `screenshots/wireshark_io_graph.png`
- `screenshots/kali_ping_broken.png`
- `screenshots/kali_ping_fixed.png`

## 3. ELK SIEM Setup

- Deployed Elasticsearch and Kibana on ELK-SERVER; verified services via `systemctl`.
- Configured Fleet with:
  - `ELK-fleet-server-policy` for the SIEM server.
  - `mint-system-policy` for Linux Mint victim (System + System auth logs).
- Confirmed sshd events in Kibana Discover with fields: `source.ip`, `user.name`, `event.outcome`.

**Artifacts:**

- `screenshots/elk_services_running.png`
- `screenshots/fleet_agents.png`
- `screenshots/discover_ssh_failures.png`
- Detailed commands: `docs/elk-setup-commands.md`

## 4. SSH Brute-Force Incident & Threat Hunting

- Launched Hydra brute-force from Kali (`192.168.10.131`) against SSH on `192.168.10.132` (user `victim`).
- Captured SSH traffic in Wireshark (`tcp.port == 22`) to verify real connections.
- Built Kibana dashboard:
  - Failed SSH logins over time (clear brute-force spike).
  - Top attacker IPs and usernames.
  - Query for `event.outcome: "success"` to confirm **no successful logins** from attacker IP.

**Artifacts:**

- `screenshots/hydra_bruteforce.png`
- `screenshots/wireshark_ssh.png`
- `screenshots/kibana_dashboard.png`

## 5. Key Skills Demonstrated

- IPv4 subnetting and address planning for small offices.
- Packet-level analysis with Wireshark (hierarchy, graphs, ICMP/SSH).
- Linux routing and basic network troubleshooting.
- ELK + Fleet deployment, log ingestion, and field-based queries.
- Correlating packets and logs to investigate brute-force attacks and verify impact.