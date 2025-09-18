#!/usr/bin/env python

import sys

if __name__ == "__main__":
    try:
        print(sys.argv[1].lower())
    except IndexError:
        print("none")