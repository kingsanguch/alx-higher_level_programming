#!/usr/bin/python3
"""
Log parsing
"""


import sys


def print_stats(file_size, status_codes):
    """Prints stats"""
    print("File size: {}".format(file_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))


def main():
    """Main function"""
    file_size = 0
    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            if len(data) > 2:
                file_size += int(data[-1])
                status_code = data[-2]
                if status_code in status_codes:
                    status_codes[status_code] += 1
            if count % 10 == 0:
                print_stats(file_size, status_codes)
    except KeyboardInterrupt:
        pass
    finally:
        print_stats(file_size, status_codes)


if __name__ == "__main__":
    main()
