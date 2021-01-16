import random

from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from bot.schema import Mutation, Query

endpoint = HTTPEndpoint("http://ec2-54-67-29-122.us-west-1.compute.amazonaws.com:3200/")


class ApiException(Exception):
    pass


def do_op(op, token=None):
    headers = None
    if token is not None:
        headers = {"Authorization": token}
    json_response = endpoint(op, extra_headers=headers)
    if "errors" in json_response:
        raise ApiException(json_response["errors"])
    response = op + json_response
    return response


class User:
    DEFAULT_PASSWORD = "dumb_password"
    BOT_EMAIL_SUFFIX = "@botnet.com"

    def __init__(self, token):
        self.token = token
        self.data = self.get_user_data()


    @staticmethod
    def signup(first, last, handle, email=None, password=DEFAULT_PASSWORD):
        op = Operation(Mutation)
        signup = op.signup(firstname=first,
                           lastname=last,
                           handle=handle,
                           email=handle + User.BOT_EMAIL_SUFFIX if email is None else email,
                           password=password)
        signup.token()

        response = do_op(op)

        user = User(response.signup.token)
        user.set_random_profile_picture()
        return user

    @staticmethod
    def from_login(email, password=DEFAULT_PASSWORD):
        op = Operation(Mutation)
        op.login(email=email, password=password)
        op.login.token()
        response = do_op(op)
        return User(response.login.token)

    def set_random_profile_picture(self):
        a = random.choice(["men", "women"])
        b = random.randint(0, 99)
        url = f"https://randomuser.me/api/portraits/{a}/{b}.jpg"
        self.edit(avatar=url)

    def edit(self, **kwargs):
        op = Operation(Mutation)
        op.edit_profile(**kwargs)
        op.edit_profile.id()
        do_op(op, token=self.token)
        self.data = self.get_user_data()

    def new_tweet(self, content, tags=None):
        if tags is None:
            tags = []
        op = Operation(Mutation)
        op.new_tweet(text=content, tags=tags)
        op.new_tweet.id()
        response = do_op(op, self.token)
        return response.new_tweet.id

    def get_user_data(self):
        op = Operation(Query)
        op.me()
        op.me.firstname()
        op.me.lastname()
        op.me.handle()
        response = do_op(op, token=self.token)
        return response.me

    @staticmethod
    def get_all_bot_emails():
        op = Operation(Query)
        op.search_by_user(term=User.BOT_EMAIL_SUFFIX)
        op.search_by_user.email()
        response = do_op(op, token=mastermind.token)
        return [user.email for user in response.search_by_user]

    def __repr__(self):
        return repr(self.data)


MASTER_BOT_EMAIL = "master@mind.com"
MASTER_BOT_PASSWORD = "iamsupersmart"
mastermind = User.from_login(MASTER_BOT_EMAIL, MASTER_BOT_PASSWORD)
