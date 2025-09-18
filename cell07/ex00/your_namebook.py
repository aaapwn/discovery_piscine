#!/usr/bin/env python

from typing import Dict


def array_of_names(names: Dict[str, str]):
    return [f"{name.capitalize()} {names[name].capitalize()}" for name in names]

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))