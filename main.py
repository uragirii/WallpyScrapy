# Read all the configurations from `config.json`

import json
import requests
import praw
import shutil
import ast
import os
import sys


#TODO:Change user agent according to the versioning
user_agent = "wallpysracpy bot v1.5 by u/NotCherub"

def check_dimension(title):
    """
    This function checks whether the dimension of the image is 16:9 or not.
    """
    title =  title.lower()
    dim_str = title[title.find('[')+1:title.find(']')]
    if dim_str == '' or dim_str is None:
        return False
    h, w = dim_str.split('x')
    h, w = int(h), int(w)
    return (h/w == 16/9)

#Load Config from config.json
config_keys = ['client_secret', 'client_id', 'destination', 'subreddits', 'upvote']
with open('config.json') as config_file:
    try:
        config = json.load(config_file)
        loaded_keys = list(config.keys())
        for key in config_keys:
            if key not in loaded_keys:
                raise AssertionError
        if ast.literal_eval(config['upvote']):
            if 'username' not in loaded_keys or 'password' not in loaded_keys:
                print("Username and Password are required for upvoting posts.") 
                raise AssertionError
        print("Succesfully loaded configuration")
    except AssertionError:
        print("The config file doesn't have enough values. Required values are {}".format(config_keys))
        sys.exit(1)
    except Exception:
        print("Config file not found.")
        sys.exit(1)

reddit = praw.Reddit(client_id = config['client_id'], client_secret = config['client_secret'], user_agent = user_agent, username = config['username'], password = config['password'])
subreddits = ast.literal_eval(config['subreddits'])
upvote = ast.literal_eval(config['upvote'])
if not os.path.exists(config['destination']):
    os.mkdir(config['destination'])
for subreddit in subreddits:
    for submission in reddit.subreddit(subreddit).hot(limit = 5):
        img_ext = submission.url.split(".")[-1]
        if img_ext not in ['png', 'jpg', 'jpeg', 'gif', 'tif', 'bmp'] and check_dimension(submission.title):
            continue
        if upvote:
            submission.upvote()
        img_url = submission.url
        img_name = submission.url.split("/")[-1]
        img_path = os.path.join(config['destination'], img_name)

        img_data = requests.get(img_url).content
        with open(img_path, 'wb') as handler:
            handler.write(img_data)
        print("Downloaded File: '{}' {}".format(img_name, submission.title))