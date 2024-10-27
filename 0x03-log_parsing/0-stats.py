#!/usr/bin/python3
import sys


total_size = 0
status_counts = {}


try:
    for i, line in enumerate(sys.stdin, 1):
        parts = line.split()
        if len(parts) < 7:
            continue

        file_size = int(parts[-1])
        status_code = parts[-2]

        total_size += file_size
        if status_code in status_counts:
            status_counts[status_code] += 1
        else:
            status_counts[status_code] = 1

        if i % 10 == 0:
            print(f"File size: {total_size}")
            for code in sorted(status_counts):
                print(f"{code}: {status_counts[code]}")


except KeyboardInterrupt:
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        print(f"{code}: {status_counts[code]}")
    raise
