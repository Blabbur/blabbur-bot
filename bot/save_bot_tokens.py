import os
from pathlib import Path
from .user import User


tokens_path = os.path.join(str(Path(__file__).parent), "tokens/tokens.txt")


def main():
    emails = User.get_all_bot_emails()
    with open(tokens_path, "w") as f:
        for email in emails:
            user = User.from_login(email, User.DEFAULT_PASSWORD)
            print("Got token", user.token, "for bot", user)
            f.write(user.token + "\n")


if __name__ == "__main__":
    main()



