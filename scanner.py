import re

LOG_FILE = "server.log"
sqli_pattern = re.compile(r"UNION\s+SELECT", re.IGNORECASE)

with open(LOG_FILE, "r") as f:
    for line in f:
        line = line.strip()
        if sqli_pattern.search(line):
            print("SQLi detected:", line)
