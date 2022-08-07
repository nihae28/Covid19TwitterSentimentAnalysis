# Covid19TwitterSentimentAnalysis
Sentiment analysis of live streaming twitter data on covid19


1.	Setup is to be made as given in requirement document - Download and Install kafka, elasticsearch and logstash along with the spark to take the streaming tweets from the twitter.
2.	Credentials to connect to twitter account is passed through command line arguments which then is used to collect tweets related to covid 19 from twitter. Then we have done sentiment analysis and sent the sentiments to elk stack.
3.	Start the logstash, zookeeper, kafka consumer and producer. Then run the .py file mentioned about in the pyspark.
4.	The program gets the streaming input of tweets from twitter and computes the sentiment analysis, then sends the logs and required sentiment data format to the logstash.
5.	Open the kibana and create index pattern as mentioned in the logstash file. Create  the dashboard to visualize the data based on time series.
6.	Cmd used to run the .py file:
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1 TwitterSentimentAnalysis.py localhost:9092 lepuri-twitter-events ‘Bearer-token’
7.	Logstash config file:


input {
kafka {
bootstrap_servers => "localhost:9092"
topics => ["lepuri-twitter-events"]
}
}
output {
elasticsearch {
hosts => ["http://localhost:9200"]
index => "ques2_assignment3"
}
}
