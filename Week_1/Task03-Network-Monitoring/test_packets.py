from scapy.all import IP, TCP, send

target_ip = "10.0.2.15"   # Kali VM eth0 address
ports = [22, 80, 443, 8080]

for p in ports:
    pkt = IP(dst=target_ip) / TCP(dport=p, flags="S")
    print(f"Sending SYN to {target_ip}:{p}")
    send(pkt, verbose=0)
