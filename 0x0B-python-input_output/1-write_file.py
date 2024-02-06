#!/usr/bin/python3
"""
Writes a string to a text file (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of characters"""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: ./1-write_file.py filename text")
        sys.exit(1)

    print(write_file(sys.argv[1], sys.argv[2]))
