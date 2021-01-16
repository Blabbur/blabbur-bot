import random

from bot.namer import random_adjective, random_noun, random_first, random_last
from bot import User
from bot.tokens import get_random_token


def random_handle():
    return random_adjective().capitalize() + random_noun().capitalize() + str(random.randint(0, 1000))


def make_bot():
    print("Creating user...")
    new_user = User.signup(random_first(), random_last(), random_handle())
    print(new_user)


def random_bot():
    return User(get_random_token())


def main():
    print("Getting random bot user:")
    bot = random_bot()
    print(bot)


if __name__ == "__main__":
    main()
