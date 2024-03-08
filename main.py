
import tweepy
import time

access_token="1588896639149711367-6NPpdTuIZTYab1ZFaVR2C2IwHbPd5M"
access_token_secret="Mt6hGciXjxB91COOXrboVdwR8Y08ttJPH7LpuCIAOu5Kd"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAIvSsgEAAAAA3XEBk2LMAj%2BuI7MGP7i%2BamdSTAc%3DIIxDW6KiE03Mug9kArQsVTgZuoCnITjwhJShfNGHSDqKcV9J3I"
api_key = "NSqapwvva60OiwCGFyjECwMYD"
api_secret ="bH3UY5CzrB1LWnIC51nhNk1zEALvF7FNf4izFxLaf25PnNiGZD"
client_id = "M0ZhTWt3elFIckp3Q3d4bm5OWlI6MTpjaQ"
client_secret = "qoFciMpVz_DX29DXKlMK0_nyXwdEhx39p0ptClIJATq_F1Jjfb"

client = tweepy.Client(bearer_token,api_key,api_secret,access_token,access_token_secret)
auth= tweepy.OAuth1UserHandler(api_key,api_secret,access_token,access_token_secret)
api= tweepy.API(auth)

while(1):

    tweet_text = input("Enter your tweet: ")

    client.create_tweet(text = tweet_text)
 