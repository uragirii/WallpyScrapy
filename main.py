# Read all the configurations from `config.json`

import json
import requests
import praw

#TODO:Change user agent according to the versioning
user_agent = "wallpysracpy bot v0.test.3 by u/NotCherub"

#Load Config from config.json
with open('config.json') as config_file:
    try:
        config = json.load(config_file)
    except Exception as e:
        raise ValueError("config file not found.")

reddit = praw.Reddit(client_id = config['client_id'], client_secret = config['client_secret'], user_agent = user_agent)
print(reddit.read_only)

print("-----")
for submission in reddit.subreddit('wallpaper').hot(limit=10):
    print(submission.title)
    print("--")