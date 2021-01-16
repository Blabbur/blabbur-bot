import random

from bot import User


def random_handle():
    return "test" + str(random.randint(0, 1000))


def main():
    print("Hello!!")
    new_user = User.signup("test", "tester", random_handle())
    print(new_user)


if __name__ == "__main__":
    main()
