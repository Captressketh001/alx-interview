#!/usr/bin/env python3
import sys
from collections import defaultdict

def print_statistics(total_size, status_code_counts):
    print("Total file size:", total_size)
    for status_code in sorted(status_code_counts.keys()):
        print(f"{status_code}: {status_code_counts[status_code]}")

def main():
    total_size = 0
    status_code_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parts = line.split()
            if len(parts) != 10 or parts[8] not in ("200", "301", "400", "401", "403", "404", "405", "500"):
                continue

            file_size = int(parts[9])
            total_size += file_size
            status_code = parts[8]
            status_code_counts[status_code] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_size, status_code_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_code_counts)

if __name__ == "__main__":
    main()
