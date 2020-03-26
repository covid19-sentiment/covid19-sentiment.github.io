"""
Run this file to start scraping process.
"""

import tweepy
import os
from tweets_scrape import scrapetweets
from dotenv import load_dotenv

load_dotenv()
consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')

access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

"""
# Scraping tweets on home timeline
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
"""

# Scraping tweets with search_words

# Initialise these variables:
search_words = "#Coronavirus OR #coronavirus OR #Covid-19 OR #Covid19 OR #covid-19 OR #COVID19 OR #COVID-19OR #covid19 OR #quarantine OR #lockdown"
date_since = "2020-03-03" #YYYY-MM-DD
date_until = "2020-03-23" #YYYY-MM-DD
numTweets = 100
numRuns = 1
# Call the function scraptweets
scrapetweets(search_words, date_since, date_until, numTweets, numRuns, api)
