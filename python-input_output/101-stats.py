#!/usr/bin/python3
"""
This script reads from standard input line by line and computes metrics.
It reports total file size and status code counts every 10 lines
and upon keyboard interruption.
"""
import sys


def print_stats(total_size, status_codes):
    """
    Prints the accumulated statistics.

    Args:
        total_size (int): Cumulative sum of all file sizes.
        status_codes (dict): Dictionary of status codes and their counts.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    total_size = 0
    status_codes = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            # The expected status code is the second to last element
            # The file size is the last element
            try:
                if len(parts) >= 2:
                    total_size += int(parts[-1])
                    status_code = parts[-2]
                    if status_code in status_codes:
                        status_codes[status_code] += 1
            except (ValueError, IndexError):
                # Skip lines that do not match the expected format
                pass

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        # Handle end of stream (EOF)
        print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        # Handle CTRL + C
        print_stats(total_size, status_codes)
        raise
