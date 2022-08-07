import json

import sys
from tweepy import StreamingClient, StreamRule
from kafka import KafkaProducer
import tweepy
import time
from textblob import TextBlob
import json

def json_serializer(data):
    return json.dumps(data).encode("utf-8")


class TweetSentimentAnalyse(tweepy.StreamingClient):
    
    def on_tweet(self, tweet):
        a = perform_sentimentanalysis(tweet)
        producer.send(topic, a)

def perform_sentimentanalysis(tweet):

    score = TextBlob(tweet.text).sentiment.polarity

    if score < 0:
        return 'Negative'

    elif score ==0:
        return 'Neutral'

    else:
        return 'Positive'


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("""
        Usage: structured_kafka_wordcount.py <bootstrap-servers> <topic> <bearertoken>
        """, file=sys.stderr)
        sys.exit(-1)

    bootstrapServers = sys.argv[1]
    topic = sys.argv[2]
    bearertoken = sys.argv[3]

    producer = KafkaProducer(bootstrap_servers=[bootstrapServers], value_serializer=json_serializer)

    printer = TweetSentimentAnalyse(bearertoken)

    rule = tweepy.StreamRule("#covid19 lang:en -is:retweet -is:reply")

    printer.add_rules(rule)

    printer.filter()

