from collections import Counter

log_file = "logs/sni_log.txt"
output_file = "logs/sni_summary.txt"
snis = []

with open(log_file, "r") as f:
    for line in f:
        if "SNI found:" in line:
            sni = line.split("SNI found:")[1].strip()
            snis.append(sni)

counts = Counter(snis)

with open(output_file, "w") as out:
    for sni, count in counts.most_common():
        out.write(f"{sni}: {count}\n")

print(f"[+] Frequency summary written to {output_file}")
