from user import User
import tweepy
from os import environ
from dotenv import load_dotenv
import time
import re

load_dotenv()

consumer_key = environ.get('API_CONSUMER_KEY')
consumer_secret = environ.get('API_CONSUMER_KEY_SECRET')

access_token = environ.get('ACCESS_TOKEN')
access_token_secret = environ.get('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

login_file = open('newslogins.txt','r')

orgs = []

for line in login_file.readlines()[1:]:
	line = line.rstrip('\n')
	org = line.split(',')
	# org syntax: [firstname,lastname,handle,email,password,twitterhandle]
	orgs.append([User.from_login(org[3], org[4]), org[5],''])

while 1:
	for org in orgs:
		print(org[1])
		tweet = api.user_timeline(org[1], count=1, tweet_mode='extended')[0]
		try:
			tweet_text = tweet.retweeted_status.full_text
		except AttributeError:  # Not a Retweet
			tweet_text = tweet.full_text
		if(tweet_text != org[2]):
			org[2] = tweet_text
			tweet_text = re.sub(r"http\S+", "", tweet_text)
			tweet_hashtags = tweet.entities['hashtags']
			org[0].new_tweet(tweet_text,tweet_hashtags)
	time.sleep(60)
