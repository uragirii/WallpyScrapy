# Read all the configurations from `config.json`

import json
import requests
import praw
import shutil
import ast
import os


#TODO:Change user agent according to the versioning
user_agent = "wallpysracpy bot v0.test.3 by u/NotCherub"

#Load Config from config.json
#TODO: Check config file before moving forward
#TODO: add option to upvote downloaded files
with open('config.json') as config_file:
    try:
        config = json.load(config_file)
        print("Succesfully loaded configuration")
    except Exception as e:
        raise ValueError("Config file not found.")

reddit = praw.Reddit(client_id = config['client_id'], client_secret = config['client_secret'], user_agent = user_agent)

subreddits = ast.literal_eval(config['subreddits'])
if not os.path.exists(config['destination']):
    os.mkdir(config['destination'])
for subreddit in subreddits:
    for submission in reddit.subreddit(subreddit).hot(limit = 5):
        #TODO:check if its an image or not
        img_url = submission.url
        img_name = submission.url.split("/")[-1]
        img_path = os.path.join(config['destination'], img_name)

        img_data = requests.get(img_url).content
        with open(img_path, 'wb') as handler:
            handler.write(img_data)
        print("Downloaded File '{}' ".format(img_name))