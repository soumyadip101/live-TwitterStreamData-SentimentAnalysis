import twitterApiSetup
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from textblob import TextBlob

# method to do sentiment analysis using TextBlob
def sentimentAnalysis(text):
	# encoded_text = urllib.quote(text)
	analysis = TextBlob(text)
	return analysis.sentiment.polarity


ckey = twitterApiSetup.CONSUMER_KEY
csecret = twitterApiSetup.CONSUMER_SECRET
atoken = twitterApiSetup.TWITTER_APP_KEY
asecret = twitterApiSetup.TWITTER_APP_SECRET

class Listener(StreamListener):
	def on_status(self, status):
		# Skip the retweets
		if status.retweeted==True:
			return True
		tweet = status.text
		print(tweet)
		# Extract the sentiment polarity for each tweet
		sentimentRating = sentimentAnalysis(tweet)
		# Categorize the polarity into three groups: 'pos', 'neg' and 'neutral'
		if sentimentRating > 0.0:
			save = tweet+'::'+str(sentimentRating)+'::pos\n'
		elif sentimentRating < 0.0:
			save = tweet+'::'+str(sentimentRating)+'::neg\n'
		else:
			save = tweet+'::'+str(sentimentRating)+'::neutral\n'
		# Store the tweets along with there sentiments in an output file
		output = open('output.txt','a', encoding='utf-8')
		output.write(save)
		output.close()
		return True
		
	def on_error(self, status):
		if status_code == 420:
			return False

# Authentication for connecting to twitter api
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
# Extract live tweet feed from twitter
twitterStream = Stream(auth, Listener())
twitterStream.filter(track = twitterApiSetup.TRACK_TERMS)

