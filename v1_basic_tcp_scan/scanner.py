import socket
from datetime import datetime

def scan_port(host, port, timeout=0.5):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)

        result = s.connect_ex((host, port))
        s.close()

        return result == 0  # True if open

    except Exception:
        return False


def scan_host(host, ports):
    print(f"\nStarting scan on {host}")
    print(f"Time: {datetime.now()}\n")

    try:
        ip = socket.gethostbyname(host)
        print(f"Target IP: {ip}\n")

    except socket.gaierror:
        print("Hostname could not be resolved")
        return

    open_ports = []
    closed_count = 0

    for port in ports:
        is_open = scan_port(ip, port)

        if is_open:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)
        else:
            closed_count += 1

    print("\n--- Scan Complete ---")

    if open_ports:
        print("\nOpen ports found:")
        for p in open_ports:
            print(f"  - {p}")
    else:
        print("\nNo open ports found.")

    print(f"\nClosed ports: {closed_count}")


if __name__ == "__main__":
    target = input("Enter target (IP or domain): ")

    # default scan range like a basic Nmap scan
    ports = range(1, 1025)

    scan_host(target, ports)
