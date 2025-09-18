#!/usr/bin/env python

from typing import Dict


def famous_births(persons: Dict[str, Dict[str, str]]):
    for _, info in sorted(persons.items(), key=lambda item: int(item[1]["date_of_birth"])):
        print(f"{info['name']} is a great scientist born in {info['date_of_birth']}.")

women_scientists = {
    "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "cecilia": {"name": "Cecilia Payne", "date_of_birth": "1900"},
    "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
    "grace": {"name": "Grace Hopper", "date_of_birth": "1906"}
}

famous_births(women_scientists)

