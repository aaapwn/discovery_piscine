#!/usr/bin/env python

age = int(input("Please tell me your age: "))

print(f"You are currently {age} years old.")

for i in range(1, 4):
    print(f"In {10 * i} years, you will be {age + 10 * i} years old.")