import random
import os
from pathlib import Path

d = str(Path(__file__).parent)

with open(os.path.join(d, "nouns.txt")) as nouns:
    noun_pool = list(map(lambda s: s[:-1], nouns.readlines()))

with open(os.path.join(d, "adjectives.txt")) as adjectives:
    adjective_pool = list(map(lambda s: s[:-1], adjectives.readlines()))

with open(os.path.join(d, "firsts.txt")) as firsts:
    first_pool = list(map(lambda s: s[:-1], firsts.readlines()))

with open(os.path.join(d, "lasts.txt")) as lasts:
    last_pool = list(map(lambda s: s[:-1], lasts.readlines()))


def random_noun():
    return random.choice(noun_pool)


def random_adjective():
    return random.choice(adjective_pool)


def random_first():
    return random.choice(first_pool)


def random_last():
    return random.choice(last_pool)

