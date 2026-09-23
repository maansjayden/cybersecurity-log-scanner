import re

LOG_FILE = "server.log"
sqli_pattern = re.compile(r"UNION\s+SELECT", re.IGNORECASE)
ip_pattern = re.compile(r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
status_pattern = re.compile(r'"\s+(\d{3})\s+')

with open(LOG_FILE, "r") as f:
    for line in f:
        line = line.strip()
        ip_match = ip_pattern.search(line)
        ip = ip_match.group(1) if ip_match else "UNKNOWN"
        # print("parsed ip:", ip)
