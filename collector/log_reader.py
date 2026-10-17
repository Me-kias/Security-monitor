from parser.log_parser import parse_log
LOG_FILE = "/var/log/auth.log"

def read_logs():
    with open(LOG_FILE, "r") as file:
        for line in file:
            yield line.strip()
        
for log in read_logs():
    event = parse_log(log)
    
if __name__ == "__main__":
    for log in read_logs():