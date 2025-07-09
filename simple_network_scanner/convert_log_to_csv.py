import csv
from datetime import datetime

log_file = "logs/sni_log.txt"
csv_file = "logs/sni_log.csv"

entries = []

# Read and parse the log
with open(log_file, "r") as f:
    for line in f:
        if "SNI found:" in line:
            try:
                timestamp_part = line.split(']')[0].strip('[')
                sni = line.split("SNI found:")[1].strip()
                entries.append((timestamp_part, sni))
            except Exception as e:
                continue

# Write to CSV
with open(csv_file, "w", newline='') as csvf:
    writer = csv.writer(csvf)
    writer.writerow(["Timestamp", "SNI"])
    writer.writerows(entries)

print(f"[+] Converted {len(entries)} entries to {csv_file}")
