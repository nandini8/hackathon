#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API

from datetime import datetime, timedelta

access_token = '941534431646330881-swNBwYQsuPZP4yd3UMo0gNXIyyENO0f'
access_token_secret = '2mMoFY3HzeWerXNIaGl6f4VMCLoSSsAgTJZAZjLuAMk6Z'
consumer_key = 'bxHiTcKEDH0Drr6ntpKnlA2FV'
consumer_secret = '2QOs9ux6gMt0FSIEfs4OqLWGHwAhhg3VX84oEpSgRlg0x6rVbh'


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l, tweet_mode='extended')
    api = API(auth)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(locations=[68.1766451354, 7.96553477623, 97.4025614766, 35.4940095078])

    stream.filter(locations=[68.109700, 6.462700,97.395359, 35.508701])
    #print(api.me())