#!/usr/bin/env python

import sys

def downcase_it(text):
    return text.lower()

if __name__ == "__main__":
    if len(sys.argv[1:]) > 0:
        for i in sys.argv[1:]:
            print(downcase_it(i))
    else:
        print("none")