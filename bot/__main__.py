import random

from bot.namer import random_adjective, random_noun, random_first, random_last
from bot import User


def random_handle():
    return random_adjective().capitalize() + random_noun().capitalize() + str(random.randint(0, 1000))


def main():
    print("Creating user...")
    new_user = User.signup(random_first(), random_last(), random_handle())
    print(new_user)
    print("Listing bot emails")
    bots = list(User.get_all_bot_users())



if __name__ == "__main__":
    main()
