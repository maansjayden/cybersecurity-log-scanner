LOG_FILE = "server.log"

with open(LOG_FILE, "r") as f:
    for line in f:
        print(line.strip())
