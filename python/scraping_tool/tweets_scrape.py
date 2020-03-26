
"""
Used to scrape Tweets that contain search words specified by user (E.g. "Coronavirus", "Covid19", "Quarantine")
"""
import tweepy
import pandas as pd
import time
import csv
import os
from nltk_main import analyze_sentiment

def scrapetweets(search_words, date_since, date_until, numTweets, numRuns, api):

    # Define a pandas dataframe to store the date:
    db_tweets = pd.DataFrame(columns = ['location', 'text', 'hashtags', 'sentiment']
                                )
    program_start = time.time()
    for i in range(0, numRuns):
        # We will time how long it takes to scrape tweets for each run:
        start_run = time.time()

        # Collect tweets using the Cursor object
        # .Cursor() returns an object that you can iterate or loop over to access the data collected.
        # Each item in the iterator has various attributes that you can access to get information about each tweet
        tweets = tweepy.Cursor(api.search, q=search_words, lang="en", since=date_since, until=date_until, tweet_mode='extended').items(numTweets)
        # Store these tweets into a python list
        tweet_list = [tweet for tweet in tweets]
        ntweets = 0

        for tweet in tweet_list:
            # Pull the values
            location = tweet.user.location
            hashtags = tweet.entities['hashtags']
            try:
                text = tweet.retweeted_status.full_text
            except AttributeError:  # Not a Retweet
                text = tweet.full_text

            # Calculate sentiment score
            sentiment = analyze_sentiment(text)

            # Store to pandas DataFrame
            ith_tweet = [location, text, hashtags, sentiment]
            db_tweets.loc[len(db_tweets)] = ith_tweet
            ntweets += 1

        # Run ended:
        end_run = time.time()
        duration_run = round((end_run-start_run)/60, 2)

        print('no. of tweets scraped for run {} is {}'.format(i + 1, ntweets))
        print('time take for {} run to complete is {} mins'.format(i+1, duration_run))

        #time.sleep(920) #15 minute sleep time

    # Once all runs have completed, save them to a single csv file:
    from datetime import datetime

    # Obtain timestamp in a readable format
    to_csv_timestamp = datetime.today().strftime('%Y%m%d_%H%M%S')
    # Define working path and filename
    path = os.getcwd()
    filename = path + '/data/' + to_csv_timestamp + '_corona_tweets.csv'
    # Store dataframe in csv with creation date timestamp
    db_tweets.to_csv(filename, index = False)

    program_end = time.time()

    print('Scraping has completed!')
    print('Total time taken to scrap is {} minutes.'.format(round(program_end - program_start)/60, 2))
