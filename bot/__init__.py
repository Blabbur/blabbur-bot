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

    def __init__(self, token, fast=False):
        self.token = token
        if not fast:
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
        op.me.id()
        op.me.firstname()
        op.me.lastname()
        op.me.handle()
        response = do_op(op, token=self.token)
        return response.me

    def follow_user(self, other_user_id):
        op = Operation(Mutation)
        op.follow(id=other_user_id)
        do_op(op, self.token)

    def get_random_unfollowed_user(self):
        op = Operation(Query)
        op.users.id()
        response = do_op(op, self.token)
        return response.users[0]

    def get_feed_content(self, include_own=False):
        op = Operation(Query)
        op.feed.tags()
        op.feed.text()
        op.feed.id()
        op.feed.is_tweet_mine()
        op.feed.is_retweet()
        op.feed.is_like()
        response = do_op(op, self.token)
        feed = response.feed
        if include_own:
            return feed
        return list(filter(lambda tweet: not tweet.is_tweet_mine, feed))

    def toggle_retweet(self):
        pass

    def get_tweet_comments(self, tweet_id, include_own=False):
        op = Operation(Query)
        op.tweet(id=tweet_id)
        op.tweet.comments.id()
        op.tweet.comments.text()
        op.tweet.comments.is_comment_mine()
        response = do_op(op, self.token)
        comments = response.tweet.comments
        if include_own:
            return comments
        return list(filter(lambda comment: not comment.is_comment_mine, comments))

    def toggle_retweet(self):
        pass

    def get_own_tweets(self):
        op = Operation(Query)
        op.me.tweets()
        op.me.tweets.id()
        op.me.tweets.text()
        op.me.tweets.tags()
        response = do_op(op, token=self.token)
        return response.me.tweets


    ######################
    # MAIN BOT ACIONS    #
    ######################

    def bot_tweet(self):
        pass

    def bot_reply(self):
        pass

    def bot_like(self):
        pass

    def bot_retweet(self):
        tweets = self.get_feed_content(include_own=False)
        for tweet in tweets:
            if tweet.is_retweet:
                continue
            if random.random() > 0.5:
                continue
            self.toggle_retweet(tweet.id)



    def bot_follow(self):
        user = self.get_random_unfollowed_user()
        self.follow_user(user.id)

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
