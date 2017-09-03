import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
from textblob import TextBlob
ckey = ''
csecret= ''
atoken = ''
asecret = ''

class listener(StreamListener):
	def on_data(self, data):
		try:
			#print(data)
			tweet = data.split(',"text":"')[1].split('","source')[0]
			print(tweet)
			saveThis = str(time.time()) + '::' + tweet
			saveFile = open('twitDB.csv', 'a')
			saveFile.write(saveThis)
			#saveFile.write(data)
			saveFile.write('\n')
			saveFile.close()
			return True
		except BaseException(e):
			print('failed ondata,', str(e))
			time.sleep(5)

	def on_error(self, status):
		print(status)
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track =["car"])
#api = tweepy.API(auth)
#public_tweets = api.search('Dog')
#for tweet in public_tweets:
#	print(tweet.text)
#	analysis = TextBlob(tweet.text)
#	print(analysis.sentiment)