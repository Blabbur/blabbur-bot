import random
from threading import Thread

from namer import random_adjective, random_noun, random_first, random_last
from user import User
from tokens import get_random_token, get_all_tokens


def random_handle():
    return random_adjective().capitalize() + random_noun().capitalize() + str(random.randint(0, 1000))


def make_bot():
    print("Creating user...")
    new_user = User.signup(random_first(), random_last(), random_handle())
    print(new_user)


def random_bot():
    return User(get_random_token())


def bot_thread():
    for i in range(0, 100):
        bot = random_bot()
        print(bot)
        bot.bot_action()

# MEDIA CORP IDS:
# AP:  ckk0dwi5c15qc0999yvbvgj05
# CNN: ckk0ifllb1ir50999l2kxopa2
# MSNBC:ckk0jn1hqoiie0a26b5mnuptx

def follow_by_all_bots(user_id):
    for token in get_all_tokens():
        print(token)
        user = User(token, fast=True)
        user.follow_user("ckk0dwi5c15qc0999yvbvgj05")
        user.follow_user("ckk0ifllb1ir50999l2kxopa2")
        user.follow_user("ckk0jn1hqoiie0a26b5mnuptx")
        print("Followed")


def main():
    threads = []
    for i in range(5):
        thread = Thread(target=bot_thread)
        thread.start()
        threads.append(thread)


if __name__ == "__main__":
    main()
