# Live Twitter Data Sentiment Analysis
This application analyzes the sentiments of live tweets from twitter by classifying them as positive and negative tweets using TextBlob and then visualizes the live sentiment trend of the search words using a line graph.
- `tweepy` library is used for tweet extraction using a Twitter API
- `textblob` library is used for sentiment analysis using the tweets
- `matplotlib` library is used to generate a real time graphing of the live tweets. 

## Installation
- `pip install -r requirements.txt`

## Setup
- Sign up for a Twitter [developer account](https://developer.twitter.com/). 
- Create an application [here](https://developer.twitter.com/en/apps).
- Set the following keys in `twitterApiSetup.py`. You can get these values from the app you created:
- `CONSUMER_KEY`
- `CONSUMER_SECRET`
- `TWITTER_APP_KEY`
- `TWITTER_APP_SECRET`

## Usage
- `python tweet_extract.py` -- to scrape tweets from twitter using tweepy and also classify the sentiment of each tweet. Use `Ctrl + C` to stop. This process will also generate an output file named 'tweets.txt' containg all the tweets and their corresponding sentiments.
- `python plot_twitter_data.py` -- to generate a live line graph showing the sentiment trend of the searched word. This process will continuously read from the outplut file 'tweets.txt' and updated the line graph.
- If you want to edit search words, they can be changed in `twitterApiSetup.py` file in the list `TRACK_TERMS`.
