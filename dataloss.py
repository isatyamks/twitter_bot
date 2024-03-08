
import tweepy

access_token="1588896639149711367-45Nx1UIb9XfOQImVLZ3QaqWKYtJTOV"
access_token_secret="B1DoHPdZuGc3ln8doHnVmcgPznTBH6nsWZDQAzWDLpUfd"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAIvSsgEAAAAAk%2BdtSrFjufAHhqI%2B%2F52skRv66V8%3DjZOzNKwVy0WCZPipLOmLXvHrLuQ5AzzQHYovs1o0ZIe2WOXfdN"
api_key = "V8q0KLSNmc4d18IeWm2dRlaYF"
api_secret ="A5vg39RmR908eZwumqOrcXQmnKVEejDYaIhYp25ust3jCqUWos"
client_id = "M0ZhTWt3elFIckp3Q3d4bm5OWlI6MTpjaQ"
client_secret = "DmpM7taHjaZozAfJMfYdcHWY_kRzKTeW0dp4zuv2snmiD97JLS"

client = tweepy.Client(bearer_token,api_key,api_secret,access_token,access_token_secret)
auth= tweepy.OAuth1UserHandler(api_key,api_secret,access_token,access_token_secret)
api= tweepy.API(auth)





class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        
        try:
            client.retweet(tweet.id)
        
        except Exception as error:
            print(error)

stream = MyStream(bearer_token = bearer_token)

rule = tweepy.StreamRule("(artificial intelligence AND neuralink)(-is:retweet -is:reply)" )

stream.add_rules(rule)

stream.filter()