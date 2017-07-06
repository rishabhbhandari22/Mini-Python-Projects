import twitter
import json

CONSUMER_KEY = '<Your Key>'
CONSUMER_SECRET = '<Your Key>'
OAUTH_TOKEN = '<Your Key>'
OAUTH_TOKEN_SECRET = '<Your Key>'
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

country_id = {'World': 1,'UK': 23424975,'Pakistan':23424922, 'India': 2295420, 'USA': 23424977, 'Japan': 1118129, 'Nigeria': 23424908, 'South Africa': 23424942, 'Canada': 23424775,'Argentina' :23424747}

print "Choose amongst the following. \n"

for country in country_id.keys():
    print country
while(1):
    country = raw_input("Country:")
    if country_id.has_key(country):
        print 'The top  trending topics in ' +country+' are:'
        print '------------------------------\n'
        PLACE_WOE_ID = country_id[country]
        place_trends = twitter_api.trends.place(_id=PLACE_WOE_ID)
        count = 1
        for trend in place_trends[0]['trends']:
            print str(count) + ') ' + trend['name']
            count+=1
        print '\nThank You for using the service.'

    else:
        print 'Information for that country is not available.'
