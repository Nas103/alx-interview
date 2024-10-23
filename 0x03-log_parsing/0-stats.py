#!/usr/bin/python3
import sys
import signal


# Initialize variables
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Print accumulated metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def handle_interrupt(signum, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)

# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) < 7:
                continue

            # Extract file size and status code
            file_size = int(parts[-1])
            status_code = int(parts[-2])

            # Update metrics
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1

            line_count += 1

            # Print stats after every 10 lines
            if line_count % 10 == 0:
                print_stats()

        except (ValueError, IndexError):
            # Skip lines with invalid data
            continue

except KeyboardInterrupt:
    # Handle CTRL + C when it's triggered during data processing
    print_stats()
    raise