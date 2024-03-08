class MyStream(tweepy.StreamingClient):
#     def on_tweet(self, tweet):
#         print(tweet.text)
        
#         try:
#             client.retweet(tweet.id)
        
#         except Exception as error:
#             print(error)

# stream = MyStream(bearer_token = bearer_token)

# rule = tweepy.StreamRule("(nasa)(-is:retweet -is:reply)" )

# stream.add_rules(rule)

# stream.filter()