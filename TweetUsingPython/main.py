
CONSUMER_KEY ='<Your Key>'
CONSUMER_SECRET = '<Your Key>'
OAUTH_TOKEN ='<Your Key>'
OAUTH_TOKEN_SECRET = '<Your Key>'

from twitter import OAuth, Twitter
auth = OAuth(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET)
t = Twitter(auth = auth)

tweet = "Tweet Using python Script"

t.statuses.update(status = tweet)
