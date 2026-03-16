import nmap
from datetime import datetime

def run_scan(target_ip):
    # Create Nmap scanner object
    scanner = nmap.PortScanner()

    # Run SYN scan on the target
    print(f"[+] Running SYN scan on {target_ip} ...")
    scanner.scan(target_ip, arguments='-sS')

    # Prepare results
    open_ports = []

    # Check if target exists in results
    if target_ip in scanner.all_hosts():
        host = target_ip
    else:
        print("[!] Target not found in scan results.")
        return None, []

    # Check TCP ports
    if 'tcp' in scanner[host]:
        for port in scanner[host]['tcp']:
            port_data = scanner[host]['tcp'][port]
            if port_data['state'] == 'open':
                service = port_data.get('name', 'unknown')
                open_ports.append((port, service))

    return host, open_ports


def write_report(target_ip, host, open_ports, filename="scan_report.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "w") as f:
        f.write("Scan Report – Task 01 (Nmap Automation)\n")
        f.write("CyArt SOC Internship\n\n")

        f.write(f"Scan Timestamp : {timestamp}\n")
        f.write(f"Target IP      : {target_ip}\n")
        f.write("Scan Type      : SYN scan (-sS)\n\n")

        f.write("Open Ports and Services:\n")
        if open_ports:
            for port, service in open_ports:
                f.write(f"- {port}/tcp  open  {service}\n")
        else:
            f.write("- No open TCP ports found.\n")

        f.write("\nScan completed successfully.\n")

    print(f"[+] Report written to {filename}")


if __name__ == "__main__":
    target = input("Enter target IP (e.g., 192.168.1.3): ").strip()

    if not target:
        print("No target provided. Exiting.")
    else:
        host, ports = run_scan(target)
        if host is not None:
            write_report(target, host, ports)
