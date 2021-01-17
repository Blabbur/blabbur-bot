import random
import urllib.error

from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from schema import Mutation, Query
from gpt3_interaction import reply_to_thread, random_new_tweet

endpoint = HTTPEndpoint("http://ec2-54-67-29-122.us-west-1.compute.amazonaws.com:3200/")


class ApiException(Exception):
    pass


def do_op(op, token=None):
    while True:
        try:
            headers = None
            if token is not None:
                headers = {"Authorization": token}
            json_response = endpoint(op, extra_headers=headers)
            if "errors" in json_response:
                raise ApiException(json_response["errors"])
            response = op + json_response
            return response
        except urllib.error.URLError:
            print("Recovered from error")


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
        op.feed.is_liked()
        op.feed.user.firstname()
        op.feed.user.lastname()
        op.feed.user.handle()
        response = do_op(op, self.token)
        feed = response.feed
        if include_own:
            return feed
        return list(filter(lambda tweet: not tweet.is_tweet_mine, feed))

    def get_tweet_comments(self, tweet_id, include_own=False):
        op = Operation(Query)
        op.tweet(id=tweet_id)
        op.tweet.comments.id()
        op.tweet.comments.text()
        op.tweet.comments.user.firstname()
        op.tweet.comments.user.lastname()
        op.tweet.comments.user.handle()
        op.tweet.comments.is_comment_mine()
        response = do_op(op, self.token)
        comments = response.tweet.comments
        if include_own:
            return comments
        return list(filter(lambda comment: not comment.is_comment_mine, comments))

    def toggle_retweet(self, tweet_id):
        op = Operation(Mutation)
        op.toggle_retweet(id=tweet_id)
        do_op(op, self.token)

    def toggle_like(self, tweet_id):
        op = Operation(Mutation)
        op.toggle_like(id=tweet_id)
        do_op(op, self.token)

    def get_own_tweets(self):
        op = Operation(Query)
        op.me.tweets()
        op.me.tweets.id()
        op.me.tweets.text()
        op.me.tweets.tags()
        response = do_op(op, token=self.token)
        return response.me.tweets

    def add_comment(self, tweet_id, reply_text):
        op = Operation(Mutation)
        op.add_comment(id=tweet_id, text=reply_text)
        op.add_comment.id()
        do_op(op, self.token)

    def do_random_reply(self, tweet):
        comments = self.get_tweet_comments(tweet.id, include_own=True)
        context = {
            "me_first": self.data.firstname,
            "me_last": self.data.lastname,
            "me_handle": self.data.handle,
            "root": {
                "text": tweet.text,
                "author_first": tweet.user.firstname,
                "author_last": tweet.user.lastname,
                "author_handle": tweet.user.handle,
            },
            "replies": [
                {
                    "text": comment.text,
                    "author_first": comment.user.firstname,
                    "author_last": comment.user.lastname,
                    "author_handle": comment.user.handle,
                }
                for comment in comments
            ]
        }
        reply_text = reply_to_thread(context)
        print("REPLY:", reply_text)
        self.add_comment(tweet.id, reply_text)

    def do_random_new_tweet(self):
        content = random_new_tweet()
        print("TWEET:", content)
        self.new_tweet(content)

    ######################
    # MAIN BOT ACIONS    #
    ######################

    def bot_tweet(self):
        print("BOT Tweet")
        self.do_random_new_tweet()

    def bot_reply(self):
        print("BOT Reply")
        tweets = self.get_feed_content(include_own=True)
        for tweet in tweets:
            if random.random() > 1:
                continue
            self.do_random_reply(tweet)
            return

    def bot_like(self):
        print("BOT Like")
        tweets = self.get_feed_content(include_own=False)
        for tweet in tweets:
            if tweet.is_liked:
                continue
            if random.random() > 0.5:
                continue
            self.toggle_like(tweet.id)
            return

    def bot_retweet(self):
        print("BOT Retweet")
        tweets = self.get_feed_content(include_own=False)
        for tweet in tweets:
            if tweet.is_retweet:
                continue
            if random.random() > 0.5:
                continue
            self.toggle_retweet(tweet.id)
            return

    def bot_follow(self):
        print("BOT Follow")
        user = self.get_random_unfollowed_user()
        self.follow_user(user.id)

    def bot_action(self):
        weights = [
            (self.bot_follow, 1),
            (self.bot_tweet, 10),
            (self.bot_reply, 20),
            (self.bot_retweet, 30),
            (self.bot_like, 40),
        ]
        args = list(zip(*weights))
        action = random.choices(args[0], weights=args[1])[0]
        action()

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
