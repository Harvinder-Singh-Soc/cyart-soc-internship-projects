#!/bin/bash

# Flush existing rules
iptables -F
iptables -X

# Set default policies
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Allow loopback traffic
iptables -A INPUT -i lo -j ACCEPT

# Allow established and related connections
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Allow SSH (port 22)
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Allow HTTP (port 80)
iptables -A INPUT -p tcp --dport 80 -j ACCEPT

# (Optional) Allow ICMP ping
# iptables -A INPUT -p icmp -j ACCEPT

# Log dropped packets (optional, can be noisy)
# iptables -A INPUT -j LOG --log-prefix "IPTABLES-DROP: " --log-level 4
