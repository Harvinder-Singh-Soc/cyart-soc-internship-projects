from scapy.all import sniff, TCP, UDP, ICMP
import matplotlib.pyplot as plt

def main():
    interface = input("Enter interface name (e.g., eth1): ")

    print(f"[+] Sniffing on interface: {interface}")
    packets = sniff(iface=interface, count=100)

    print(f"[+] Captured packets: {len(packets)}")

    protocol_counts = {"TCP": 0, "UDP": 0, "ICMP": 0, "OTHER": 0}

    for pkt in packets:
        if pkt.haslayer(TCP):
            protocol_counts["TCP"] += 1
        elif pkt.haslayer(UDP):
            protocol_counts["UDP"] += 1
        elif pkt.haslayer(ICMP):
            protocol_counts["ICMP"] += 1
        else:
            protocol_counts["OTHER"] += 1

    print("[+] Protocol distribution:")
    for proto, count in protocol_counts.items():
        print(f"{proto}: {count}")

    # Yaha se chart ka code start
    protocols = list(protocol_counts.keys())
    counts = list(protocol_counts.values())

    plt.figure(figsize=(6, 4))
    plt.bar(protocols, counts, color=['blue', 'green', 'orange', 'red'])
    plt.xlabel("Protocols")
    plt.ylabel("Packet Count")
    plt.title("Protocol Distribution (first 100 packets)")
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.savefig("protocol_distribution.png")
    print("[+] Saved bar chart as protocol_distribution.png")

if __name__ == "__main__":
    main()
