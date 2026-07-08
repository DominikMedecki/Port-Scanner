import socket
from datetime import datetime


VERSION = "PyPort Scout v2.0"


def validate_port(port):
    """
    Checks if a port number is valid.
    """

    return 1 <= port <= 65535


def scan_port(host, port, timeout=0.5):
    """
    Attempts a TCP connection to a specific port.
    
    Returns:
        True  = Port is open
        False = Port is closed/unreachable
    """

    try:
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(timeout)

        result = scanner.connect_ex((host, port))

        scanner.close()

        return result == 0

    except socket.error:
        return False


def scan_target(host, start_port, end_port):

    print("=" * 40)
    print(VERSION)
    print("=" * 40)

    print(f"\nTarget: {host}")
    print(f"Port Range: {start_port}-{end_port}")
    print(f"Scan Started: {datetime.now()}\n")


    try:
        target_ip = socket.gethostbyname(host)

        print(f"Resolved IP: {target_ip}\n")

    except socket.gaierror:
        print("[ERROR] Could not resolve target.")
        return


    open_ports = []
    closed_ports = 0


    for port in range(start_port, end_port + 1):

        if scan_port(target_ip, port):

            print(f"[OPEN] Port {port}")
            open_ports.append(port)

        else:
            closed_ports += 1


    print("\n========== Scan Summary ==========")

    print(f"Ports scanned: {end_port - start_port + 1}")

    print(f"Open ports: {len(open_ports)}")

    print(f"Closed ports: {closed_ports}")


    if open_ports:
        print("\nOpen ports found:")

        for port in open_ports:
            print(f"- {port}")

    print("\nScan completed.")
    

if __name__ == "__main__":

    print(VERSION)

    target = input("\nEnter target IP/domain: ")

    try:

        start = int(input("Starting port: "))
        end = int(input("Ending port: "))


        if not validate_port(start) or not validate_port(end):
            print("[ERROR] Ports must be between 1 and 65535.")
            exit()


        if start > end:
            print("[ERROR] Starting port cannot be higher than ending port.")
            exit()


        scan_target(target, start, end)


    except ValueError:

        print("[ERROR] Port values must be numbers.")
