#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n = len(sys.argv)
    sum = 0
    for i in range(1, n):
        sum += int(sys.argv[i])
    print(sum)
