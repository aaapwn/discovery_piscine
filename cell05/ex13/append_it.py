#!/usr/bin/env python

import sys

if __name__ == "__main__":
    if len(sys.argv[1:]) > 0:
        for i in sys.argv[1:]:
            if not i.endswith("ism"):
                print(f"{i}ism")
    else:
        print("none")