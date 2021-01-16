import openai
from dotenv import load_dotenv
import os
import random
import regex


def react_to_news():
    react_instruction = "React to the following piece of news:"
    pass


def reply_to_thread():
    pass


def random_new_tweet():
    tweet_types = ["hot-takes.txt", "jokes.txt"]
    tweets_of_category = open(f'prompts/{random.choice(tweet_types)}').read().splitlines()

    # topics = ["Trump", "Facebook", "personality tests", "LeBron James", "smoking", "cooking", "astrology"]
    prompt_tweets = random.sample(tweets_of_category, 5)
    prompt = '\n'.join(prompt_tweets) + '\n'

    load_dotenv()
    openai.api_key = os.getenv('OPENAI_SECRET')
    response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=50, stop="\n")["choices"][0]["text"]

    category_filter_regex = "^.+?:(.*)"
    regex_result = regex.match(category_filter_regex, response)
    if regex_result and len(regex_result) > 1:
        response = regex_result[1].strip()
    print(response)
