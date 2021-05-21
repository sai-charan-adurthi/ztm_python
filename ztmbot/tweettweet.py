import tweepy
import time
import configparser

configparser = configparser.ConfigParser()
auth = tweepy.OAuthHandler(configparser.get('twitter_api', 'oauthHandler'))
auth.set_access_token(configparser.get('twitter_api', 'accessToken'))

api = tweepy.API(auth)

user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)
                
#generous bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     print(follower.name)
    
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

search_string = 'python'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break