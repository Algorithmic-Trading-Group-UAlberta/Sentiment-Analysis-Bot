import tweepy
from textblob import TextBlob
# token for twitter developers
client = tweepy.Client(
    bearer_token="AAAAAAAAAAAAAAAAAAAAAH25ZgEAAAAAhYF6WxrvNdOb0Exym7bdt6kK%2F%2FE%3DyrN614bUeuyvfEakFpf6CtI2OhdOfpVOToyd9ynsRKq2cXR9Vd",
    consumer_key="UEOgvaDMQ16ialB0EPzIMbRLf",
    consumer_secret="oqNV6ZYG81udZvT23SgQLXAhi91wb3aSCIXNWNKtfMPGb7TkA5",
    access_token="1497773579747815428-851NlGtWySwE7VYBrLlnnZCUlz2ZBt",
    access_token_secret="SzW3Ah021h8U7ToEpehpMLytotqDaIlh7WaIuoSLe3pll"
)
account = str(input("Enter ID: "))
numTweets = int(input("Enter number of tweets: ")) # needs to be atleast 10
# find tweet by query
query = 'from:{} -is:retweet'.format(account) # need to read documentation for building query
tweet = client.search_recent_tweets(query = query, max_results = numTweets)

# extract txt data from tweet
for txt in tweet.data:
    blob = TextBlob(str(txt))
    sentiment = blob.sentiment.polarity
    if sentiment != 0:
        if sentiment < 0:
            print(f'{str(txt)}. SENTIMENT = {abs(sentiment)*100} negative')
            print()
        else:
            print(f'{str(txt)}. SENTIMENT = {abs(sentiment)*100} positive')
            print()
    else:
        pass