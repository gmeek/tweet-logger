# tweet-logger

Log tweets

## Installation
pip install python-twitter

## LAST_TWEET
File contains the earliest tweet id for the stream. get_tweets.py will fetch ids after this.

## tweet_reader
A simple JSONP parser used to test the tweet file format

## get_tweets.py
Reads the id from LAST_TWEET and then does a GetTimeline since that id. Stores up to 200 tweets in a file named with the previous tweet_id.

