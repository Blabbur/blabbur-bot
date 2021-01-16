import os
import random
from pathlib import Path

tokens_path = os.path.join(str(Path(__file__).parent), "tokens.txt")


with open(tokens_path) as tokens:
    token_pool = list(map(lambda s: s[:-1], tokens.readlines()))


def get_random_token():
    return random.choice(token_pool)


def get_all_tokens():
    return token_pool
