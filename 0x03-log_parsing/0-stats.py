#!/usr/bin/python3
import sys


def print_stats(total_size, status_counts):
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


if __name__ == "__main__":
    total_size = 0
    status_counts = {
            200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
            }
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()

            if len(parts) < 7:
                continue  # Skip lines that don't match the expected format

            # Parse the file size and status code
            try:
                file_size = int(parts[-1])
                status_code = int(parts[-2])
            except (ValueError, IndexError):
                continue

            total_size += file_size

            if status_code in status_counts:
                status_counts[status_code] += 1

            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, status_counts)
