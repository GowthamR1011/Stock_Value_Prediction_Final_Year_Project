import os
import tweepy as tw
import pandas as pd

consumer_key= '5H9CF1Y5FKJX14R1VSls5IaPc'
consumer_secret= 'vLDs79xYJKSGf0pot8g9GmdlHrjsp7NvJHbUOSKwKQuJDYCQQb'
access_token= '1283069149036466179-wU0gS058UsiXbZxBVm8UpCoifpulKo'
access_token_secret= 'V5lgsAF9Ja0CybJ14enR6JC8BqJItcQMduRy1HKWRGlK5'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)



def get_tweets(hashtag,company_name,media_list):
  authorized_tweets_sum = 0 
  tweet_list = []
  count = 1
  for source_name in media_list:
    search_words = hashtag 
    source = "from:{}".format(source_name)
    query = source + search_words + " -filter:retweets"

    tweets = list(tw.Cursor(api.search,q=query,lang="en").items(20))
    authorized_tweets_sum = authorized_tweets_sum + len(tweets)
    for tweet in tweets:
      tweet_list.append([count,tweet.user.screen_name,tweet.text,tweet.created_at,1])
      count = count + 1    
    

    if authorized_tweets_sum < 50:
      new_query = search_words + " -filter:retweets"

      unauth_tweets = list(tw.Cursor(api.search,q=new_query,lang="en").items(50-authorized_tweets_sum))
     
      for tweet in unauth_tweets:
        tweet_list.append([count,tweet.user.screen_name,tweet.text,tweet.created_at,0])
        count = count + 1
    return tweet_list

  