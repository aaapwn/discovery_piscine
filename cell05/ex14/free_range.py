#!/usr/bin/env python

import sys

if __name__ == "__main__":
    try:
        arr = range(int(sys.argv[1]), int(sys.argv[2]) + 1)
        print(list(arr))
    except IndexError:
        print("none")