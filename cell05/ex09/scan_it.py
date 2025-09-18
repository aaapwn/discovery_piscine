#!/usr/bin/env python

import sys
import re

if __name__ == "__main__":
    if len(sys.argv[1:]) == 2:
        search = re.findall(sys.argv[1], sys.argv[2])
        if search:
            print(len(search))
        else:
            print("none")
    else:
        print("none")