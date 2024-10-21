#!/usr/bin/python3
import sys

# Initialize variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
count = 0


def print_stats():
    """Prints the accumulated metrics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


try:
    for line in sys.stdin:
        count += 1
        parts = line.split()

        try:
            # Extract file size and status code
            file_size = int(parts[-1])
            status_code = int(parts[-2])

            # Update total file size
            total_size += file_size

            # Update status code count if valid
            if status_code in status_codes:
                status_codes[status_code] += 1

        except (ValueError, IndexError):
            # Skip lines with incorrect format
            continue

        # Print statistics after every 10 lines
        if count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print statistics when interrupted by CTRL + C
    print_stats()
    raise

# Print final statistics at the end of input
print_stats()