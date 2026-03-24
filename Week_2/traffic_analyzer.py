from typing import Dict, Any, List, Tuple
import pyshark
import matplotlib.pyplot as plt

PCAP_FILE: str = "day04_https_capture.pcapng"


def get_ips(pkt) -> Tuple[str, str]:
    """
    Try to extract source and destination IP (IPv4 or IPv6).
    Fallback to 'unknown' if not present.
    """
    if hasattr(pkt, "ip"):
        return pkt.ip.src, pkt.ip.dst
    if hasattr(pkt, "ipv6"):
        return pkt.ipv6.src, pkt.ipv6.dst
    return "unknown", "unknown"


def load_packets(pcap_path: str) -> List[Dict[str, Any]]:
    """
    Load HTTPS packets (tcp.port == 443) from a pcap file using pyshark.
    Returns a list of dictionaries with IPs and packet length.
    """
    print(f"[*] Opening pcap: {pcap_path}")
    capture = pyshark.FileCapture(
        pcap_path,
        display_filter="tcp.port == 443"
    )

    packets: List[Dict[str, Any]] = []
    raw_count: int = 0

    for i, pkt in enumerate(capture, start=1):
        raw_count += 1

        # Packet length
        try:
            length = int(pkt.length)
        except AttributeError:
            continue

        src_ip, dst_ip = get_ips(pkt)

        packets.append(
            {
                "num": i,
                "src_ip": src_ip,
                "dst_ip": dst_ip,
                "length": length,
            }
        )

    capture.close()
    print(f"[*] pyshark read packets (all): {raw_count}")
    print(f"[*] Valid packets stored: {len(packets)}")
    return packets


def plot_size_distribution(sizes: List[int]) -> None:
    """
    Create and save a polished histogram of HTTPS packet sizes.
    """
    if not sizes:
        print("[!] No packet sizes to plot – check pcap / filter.")
        return

    plt.figure(figsize=(10, 4))
    plt.hist(sizes, bins=10, edgecolor="black", color="#1f77b4")

    plt.xlabel("Packet size (bytes)", fontsize=11)
    plt.ylabel("Count", fontsize=11)
    plt.title("HTTPS Packet Size Distribution", fontsize=13, fontweight="bold")

    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig("day04_packet_size_distribution.png", dpi=300)
    plt.close()
    print("[*] Saved polished histogram: day04_packet_size_distribution.png")


def main() -> None:
    """
    Load packets from pcap, print basic stats, and generate histogram.
    """
    packets = load_packets(PCAP_FILE)
    print(f"Total HTTPS packets after parsing: {len(packets)}")

    sizes = [p["length"] for p in packets]
    if sizes:
        print(f"Min size: {min(sizes)} bytes, Max size: {max(sizes)} bytes")

    # Sample metadata (first 10 packets)
    print("\nSample packet metadata (first 10):")
    for p in packets[:10]:
        print(
            f"{p['num']:4d}: {p['src_ip']} -> {p['dst_ip']} | size={p['length']} bytes"
        )

    plot_size_distribution(sizes)


if __name__ == "__main__":
    main()
