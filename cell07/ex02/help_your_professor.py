#!/usr/bin/env python

from typing import Dict


def average(_class: Dict[str, int]):
    return sum(_class.values()) / len(_class.values())

class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

print(f"Average of class 3B: {average(class_3B)}")
print(f"Average of class 3C: {average(class_3C)}")