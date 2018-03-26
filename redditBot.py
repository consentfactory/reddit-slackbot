#!/usr/bin/python
# Created 2017.03.27 by Jimmy Taylor

# Import libraries that we need
# Reddit Python API 
import praw
# OS library
import os
# JSON library
import json
from slackclient import SlackClient

# Create connection to reddit
r = praw.Reddit('bot1')

# Connection to Slack with Slack token
token = "<token>"
sc = SlackClient(token)

# Create user agent for Reddit api

# Storing id's of submissions in a text file for now. That should eventually 
# be stored in a database, probably sqlite

# First check to see if the file exists, if it doesn't create empty array to
# store the submission ids
if not os.path.isfile("posts_replied_to.txt"): 
    posts_replied_to = []

# If the file does exist then read it in, split on the new line characters
# and filter out None as it's possible to have a blank file
else:
	with open ("posts_replied_to.txt", "r") as f:
		posts_replied_to = f.read()
		posts_replied_to = posts_replied_to.split("\n")
		posts_replied_to = list(filter(None, posts_replied_to))

# Praw call to connect to our subreddit of choice!
subreddit = r.subreddit("k12sysadmin")

# Loop through the new submissions. We're only grabbing 5 each time
for submission in subreddit.new(limit=1):
    att = [{
    "author_name": submission.author.name,
    "color": "#000000",
    "fallback": submission.url,
    "title": submission.title,
    "title_link": submission.url,
    "text": submission.selftext,
    "footer": "reddit.com/r/k12sysadmin",
    "footer_icon": "https://www.reddit.com/favicon.ico",
    }]
    if submission.id not in posts_replied_to:
        sc.api_call("chat.postMessage", username="redditbot", channel="test", 
        text="*New Post from /r/k12sysadmin*", 
        attachments=json.dumps(att),
        unfurl_links="false",
        as_user=True)
        #print("Title: ", submission.title)
        #print("Text: ", submission.selftext)
        #print("Score: ", submission.score)
        #print("---------------------------------\n")
        posts_replied_to.append(submission.id)

# Open our text file and write out the new submission.id so we don't 
# post it again.
with open("posts_replied_to.txt", "w") as f:
	for post_id in posts_replied_to:
		f.write(post_id + "\n")