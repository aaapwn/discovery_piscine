#!/usr/bin/env python

import sys

if __name__ == "__main__":
    try:
        parameter = sys.argv[1]
        text = input("What was the parameter? ")
        if parameter == text:
            print("Good job!")
        else:
            print("Nope, sorry...")
    except IndexError:
        print("none")