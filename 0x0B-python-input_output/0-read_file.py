#!/usr/bin/python3
"""
Reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """Reads a text file and prints its content"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: ./0-read_file.py filename")
        sys.exit(1)

    read_file(sys.argv[1])
