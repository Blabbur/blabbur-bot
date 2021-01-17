import openai
from dotenv import load_dotenv
import os
import random
import regex


def react_to_news():
    react_instruction = "React negatively to the following piece of news: President-elect Joe Biden introduced his slate of scientific advisers with the promise that they would summon “science and " \
                        "truth” to combat the pandemic, climate crisis and other challenges.\n"
    load_dotenv()
    openai.api_key = os.getenv('OPENAI_SECRET')
    response = openai.Completion.create(engine="davinci-instruct-beta", prompt=react_instruction, max_tokens=50, stop="\n\n")
    return response["choices"][0]["text"]


def reply_to_thread():
    pass


def random_new_tweet():
    tweet_types = ["hot-takes.txt", "jokes.txt"]
    selected_type_file = f'prompts/{random.choice(tweet_types)}'
    tweets_of_category = open(selected_type_file).read().splitlines()

    # topics = ["Trump", "Facebook", "personality tests", "LeBron James", "smoking", "cooking", "astrology"]
    prompt_tweets = random.sample(tweets_of_category, 5)
    prompt = '\n'.join(prompt_tweets) + '\n'

    load_dotenv()
    openai.api_key = os.getenv('OPENAI_SECRET')
    response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=50, stop="\n")["choices"][0]["text"]

    with open(selected_type_file, 'a') as fd:
        fd.write(f'\n{response}')
    category_filter_regex = "^.+?:(.*)"
    regex_result = regex.match(category_filter_regex, response)
    if regex_result and len(regex_result) > 1:
        response = regex_result[1].strip()
    return response


print(react_to_news())