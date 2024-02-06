#!/usr/bin/python3
"""
Appends a string at the end of a text file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """Appends a string to a text file and returns the number of characters"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: ./2-append_write.py filename text")
        sys.exit(1)

    print(append_write(sys.argv[1], sys.argv[2]))
