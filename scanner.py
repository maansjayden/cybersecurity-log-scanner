import re

LOG_FILE = "server.log"
sqli_pattern = re.compile(r"UNION\s+SELECT", re.IGNORECASE)
ip_pattern = re.compile(r"^(\d+\.\d+\.\d+\.\d+)")

with open(LOG_FILE, "r") as f:
    for line in f:
        line = line.strip()
        # regex search returning none on some lines
        ip = ip_pattern.search(line).group(1)
        print("ip:", ip)
