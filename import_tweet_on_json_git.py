#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 22:07:37 2021

@author: yurifarod
"""

import tweepy
import json
from textblob import TextBlob as tb
from googletrans import Translator

consumer_key        = "123"
consumer_secret     = "123"
access_token        = "123-123"
access_token_secret = "123"

translator = Translator()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

analysis = None
public_tweets = api.search('bolsonaro', count=10, tweet_mode="extended")
tweets_json = public_tweets[0]._json

final_json = []
for data in tweets_json:
    texto = translator.translate(tweets_json['full_text'], dest='en').text
    user = tweets_json['user']['name']
    location = tweets_json['user']['location']
    
    #calculo de polaridade
    analysis = tb(texto)
    polarity = analysis.sentiment.polarity
    
    dic = {'texto': texto, 'user': user, 'loc': location, 'pol':polarity}
    final_json.append(dic)

with open('data/dados_tweet.json', 'w') as f:
    json.dump(final_json, f)

from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, StringType, FloatType

appName = "PySpark Manipule Tweets"
master = "local"

# Create Spark session
spark = SparkSession.builder.appName(appName).master(master).getOrCreate()

# Create a schema for the dataframe
schema = StructType([
    StructField('texto', StringType(), True),
    StructField('user', StringType(), True),
    StructField('loc', StringType(), True),
    StructField('pol', FloatType(), True)
])

# Create data frame
json_file_path = 'data/dados_tweet.json'
df = spark.read.json(json_file_path, schema, multiLine=True)
print(df.schema)
df.show()