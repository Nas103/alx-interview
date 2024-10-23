#!/usr/bin/python3
import sys
import signal


def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)"""
    print_summary()
    sys.exit(0)


def print_summary():
    """Print the summary of the log parsing"""
    print("File size: {}".format(total_size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] != 0:
            print("{}: {}".format(key, status_codes[key]))


# Initialize variables
total_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) > 1:
            # Extract file size and status code
            size = int(parts[-1])
            code = parts[-2]
            total_size += size
            if code in status_codes:
                status_codes[code] += 1
except Exception as e:
    print("Error:", e)
finally:
    print_summary()
