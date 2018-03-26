# K12 Sysadmin Reddit Bot

This is a fork of reddit-slackbot that I customized for the [k12sysadmin subreddit](https://k12sysadmin.reddit.com). It's a simple Python script that I've modified a bit that basically checks for the latest posts on the subreddit, compares the current posts to a text file, and posts a summary of the post to the k12sysadmin Slack channel. 

## Where To Run This

I basically run this on the free tier of Google Cloud Compute on a small Ubuntu Server 16.04 instance as a CRON job. Runs every minute to check for posts.

## Credit

### Reddit SlackBot
https://github.com/jhwhite/reddit-slackbot

### PRAW
https://praw.readthedocs.io/en/v2.1.21/index.html

### Build a Reddit Bot
http://pythonforengineers.com/build-a-reddit-bot-part-1/

### Sending New Subreddit Posts to a Slack Channel
http://jhwhite.github.io/blog/2015/12/13/sending-new-subreddit-posts-to-a-slack-channel/


