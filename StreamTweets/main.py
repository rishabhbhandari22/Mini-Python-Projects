import tweepy
import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = '<Your Key>'
csecret = '<Your Key>'
atoken = '<Your Key>'
asecret = '<Your Key>'

class listener(StreamListener):

	def on_data(self, data):
		try:
			tweet = data.split(',"text":"')[1].split('","source')[0]
			print tweet
			saveThis = str(time.time()) + '::' + tweet
			saveFile = open('SavedTweets.csv','a')
			saveFile.write(saveThis)
			saveFile.write('\n')
			saveFile.close()
			return True
		except BaseException, e:
			pass
	def on_error(self,status):
		print status


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["India"])

