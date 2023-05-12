#!/usr/bin/python3
"""Module -> log parsing"""
import sys
import re

if __name__ == "__main__":

    total_size = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
        }
    count = 0

    def print_metrics():
        """computes & prints metrics"""
        print("File size: {}".format(total_size))
        for code in sorted(status_codes.keys()):
            if status_codes[code] > 0:
                print("{}: {}".format(code, status_codes[code]))

# Read lines from stdin
try:
    for line in sys.stdin:
        # Split line into components
        try:
            ip_address, _, _, date, _, request, status_code, file_size = line.split()
            if request != "GET /projects/260 HTTP/1.1":
                continue
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        # Update metrics
        total_size += file_size
        status_codes[code] += 1
        count += 1

        # Check if we have processed 10 lines
        if len(status_codes) % 10 == 0:
            # Print the metrics
            print_metrics()

except KeyboardInterrupt:
    # Print the metrics
    print_metrics()
