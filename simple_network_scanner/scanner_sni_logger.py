import argparse
import pyshark
import scapy.all as scapy
import os
from datetime import datetime

def scan(subnet):
    print(f"[+] Scanning for devices on {subnet}...\n")
    arp_req = scapy.ARP(pdst=subnet)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_req
    answered = scapy.srp(packet, timeout=2, verbose=False)[0]

    print("[+] Connected Devices:")
    for sent, received in answered:
        print(f"IP: {received.psrc}, MAC: {received.hwsrc}")

def sniff_https_sni(interface):
    print("[*] Reminder: For sniffing mode, your interface must be in monitor mode.")
    print(f"[+] Listening on {interface} for HTTPS (port 443) traffic...\n")

    def process_packet(pkt):
        try:
            if hasattr(pkt, 'tls') and hasattr(pkt.tls, 'handshake_extensions_server_name'):
                sni = pkt.tls.handshake_extensions_server_name
                time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{time_now}] SNI Host: {sni}")
        except Exception as e:
            pass  # silently ignore non-TLS packets

    try:
        capture = pyshark.LiveCapture(interface=interface, display_filter="tls.handshake.extensions_server_name")
        capture.apply_on_packets(process_packet)
    except Exception as e:
        print(f"[!] Error starting capture: {e}")

def main():
    parser = argparse.ArgumentParser(description="Simple Network Scanner & HTTPS SNI Logger")
    parser.add_argument("--scan", help="Scan connected devices in a subnet", action="store_true")
    parser.add_argument("--sniff", help="Sniff HTTPS packets and extract SNI", action="store_true")
    parser.add_argument("--subnet", help="Target subnet (e.g., 192.168.1.0/24)")
    parser.add_argument("--iface", help="Network interface to sniff on (monitor mode)", default="wlan0")
    args = parser.parse_args()

    if args.scan:
        if not args.subnet:
            print("[!] Please provide a subnet using --subnet <CIDR>")
        else:
            scan(args.subnet)
    elif args.sniff:
        sniff_https_sni(args.iface)
    else:
        print("[!] Please specify --scan or --sniff")

if __name__ == "__main__":
    main()

