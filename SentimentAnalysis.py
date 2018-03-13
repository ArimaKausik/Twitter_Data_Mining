
import tweepy
import csv
from tweepy import OAuthHandler
import os
Consumer_Key= #'Insert your consmer key'
Access_Secret=#'Insert your access secret'
Consumer_Secret=#'Insert your consumer secret'
Access_Key=#'Insert your access key'
auth=OAuthHandler(Consumer_Key,Consumer_Secret)
auth.set_access_token(Access_Key,Access_Secret)
api=tweepy.API(auth,wait_on_rate_limit=True)
csvFile=open('Senti.csv','w')
csvWriter=csv.writer(csvFile)
for tweet in tweepy.Cursor(api.search,q="#iPhone10",count=100,lang="en",since="2017-09-17").items(50):
    print(tweet.created_at,tweet.text)
    csvWriter.writerow([tweet.created_at,tweet.text.encode('utf-8')])
