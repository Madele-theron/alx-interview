#!/usr/bin/python3
"""Module - log parsing"""
import sys
import re

if __name__ == "__main__":
    count = 0
    total_size = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
    }


def print_metrics():
    """"""
    '''Prints accumulated statistics.'''
    print("File size: {}".format(count[0]))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))


# regex pattern to match the input format:
input_format = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[[^\]]*\] "GET \/projects\/260 HTTP\/1\.1" \d{3} \d*$'

count = 1
try:
    for line in sys.stdin:
        if re.match(input_format, line):
            if count % 10 == 0:
                print_metrics()
            count += 1
            
except KeyboardInterrupt:
    print_metrics()

