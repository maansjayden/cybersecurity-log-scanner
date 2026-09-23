import re
from collections import defaultdict

LOG_FILE = "server.log"

sqli_pattern = re.compile(r"UNION\s+SELECT", re.IGNORECASE)
ip_pattern = re.compile(r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
status_pattern = re.compile(r'"\s+(\d{3})\s+')

sqli_alerts = []
unauthorized_counts = defaultdict(int)

with open(LOG_FILE, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        ip_match = ip_pattern.search(line)
        ip = ip_match.group(1) if ip_match else "UNKNOWN"

        if sqli_pattern.search(line):
            sqli_alerts.append((ip, line))

        status_match = status_pattern.search(line)
        if status_match and status_match.group(1) == "401":
            # print("found 401 for ip:", ip)
            unauthorized_counts[ip] += 1

print("=== SERVER LOG SECURITY SCANNER REPORT ===")
print(f"Total SQL Injection Attempts: {len(sqli_alerts)}")
for ip, log_line in sqli_alerts:
    print(f"  [ALERT] SQLi from {ip} -> {log_line}")

print("\nRepeated 401 Unauthorized Incidents (Threshold >= 3):")
for ip, count in unauthorized_counts.items():
    if count >= 3:
        print(f"  [ALERT] Brute force suspect {ip} ({count} failed attempts)")
print("==========================================")
