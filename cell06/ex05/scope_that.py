#!/usr/bin/env python

def add_one(num):
    num += 1
    return num

x = 42
print("before", x)
x = add_one(x)
print("after", x)
