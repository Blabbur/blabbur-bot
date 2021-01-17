import random

from bot.namer import random_adjective, random_noun, random_first, random_last
from bot import User
from bot.tokens import get_random_token, get_all_tokens


def random_handle():
    return random_adjective().capitalize() + random_noun().capitalize() + str(random.randint(0, 1000))


def make_bot():
    print("Creating user...")
    new_user = User.signup(random_first(), random_last(), random_handle())
    print(new_user)


def random_bot():
    return User(get_random_token())


def main():
    for bot_token in get_all_tokens():
        print("Token:", bot_token)
        bot = User(bot_token)
        n = random.randint(4, 20)
        for i in range(n):
            bot.follow_random_account()
            print("Followed")
        print("Done following", n)


if __name__ == "__main__":
    main()
