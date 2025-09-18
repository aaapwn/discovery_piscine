#!/usr/bin/env python

import sys

def shrink(text):
    print(text[:8])

def enlarge(text):
    print(text + ("Z" * (8 - len(text))))

if __name__ == "__main__":
    if len(sys.argv[1:]) > 0:
        for i in sys.argv[1:]:
            if len(i) > 8:
                shrink(i)
            elif len(i) < 8:
                enlarge(i)
            else:
                print(i)
    else:
        print("none")