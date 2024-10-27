#!/usr/bin/python3
import sys
import re


status_code_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}


def print_stats():
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")


line_count = 0
total_file_size = 0


try:
    for line in sys.stdin:
        line_count += 1

        match = re.match(r'\S+ - (.*?) "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)', line)
        if match:
            status_code = int(match.group(2))
            file_size = int(match.group(3))

            total_file_size += file_size
            if status_code in status_code_count:

                status_code_count[status_code] += 1

        if line_count % 10 == 0:
            print_stats()


except Exception:
    pass
finally:
    print_stats()
