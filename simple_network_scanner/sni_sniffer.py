import argparse
import pyshark
from datetime import datetime
import os

def sniff_sni(iface):
    print("[*] Starting capture on {} for TLS Client Hello packets...".format(iface))

    # Create logs directory
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "sni_log.txt")

    # Start sniffing
    capture = pyshark.LiveCapture(interface=iface, display_filter='tls.handshake.extensions_server_name')

    try:
        for packet in capture.sniff_continuously():
            try:
                sni = packet.tls.handshake_extensions_server_name
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                log_entry = f"[{timestamp}] SNI found: {sni}"
                print(f"[+] {log_entry}")

                # Save to log file
                with open(log_file, "a") as f:
                    f.write(log_entry + "\n")

            except AttributeError:
                continue
    except KeyboardInterrupt:
        print("\n[*] Sniffing stopped by user.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sniff HTTPS SNI from TLS Client Hello packets.")
    parser.add_argument('--iface', required=True, help='Network interface to sniff on (in monitor mode)')

    args = parser.parse_args()
    sniff_sni(args.iface)
