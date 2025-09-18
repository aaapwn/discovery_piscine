#!/usr/bin/env python

import sys

if __name__ == "__main__":
    try:
        print(sys.argv[1])
    except IndexError:
        print("none")