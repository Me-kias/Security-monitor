
from parser.log_parser import parse_log

LOG_FILE = "/var/log/auth.log"


def read_logs(log_file=LOG_FILE):
    with open(log_file, "r") as file:
        for line in file:
            yield line.strip()


if __name__ == "__main__":
    for log in read_logs():
        event = parse_log(log)

        if event is not None:
            print(event)
