#!/usr/bin/python3
"""Module -> log parsing"""
import sys
import re

if __name__ == "__main__":

    total_size = 0
    status_codes = {}

    def print_metrics():
        """computes & prints metrics"""
        print(f"File size: {total_size}")
        for code, count in sorted(status_codes.items()):
            print("{}: {}".format(code, count))

    try:
        for line in sys.stdin:
            # Validate the input format
            if not re.match(
                r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[[^\]]*\] '
                r'"GET \/projects\/260 HTTP\/1\.1" \d{3} \d*$', line
            ):
                continue

            # Get status codes and file sizes
            match = re.search(r' (\d{3}) (\d+)$', line)
            status_code = match.group(1)
            file_size = int(match.group(2))

            total_size += file_size

            # Update status code dict
            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

            # Check if we have processed 10 lines
            if len(status_codes) % 10 == 0:
                # Print the metrics
                print_metrics()
    except KeyboardInterrupt:
        # Print the metrics
        print_metrics()
