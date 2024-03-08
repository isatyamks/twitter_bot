
import tweepy
import time

# access_token="158889667uIZ3136-6NPpdT9hshs14971TYab1ZBhsbFaVR2C2IwHbPd5M"
# access_token_secret="Mt6sgsgshghGcigXjxB91COOXrboVdwR8Y08ttJPjsbvvH7LpuCIAOu5Kd"
# bearer_token = r"s sjbvsEBk2LMAj%2BuI7MGP7i%2BamdSTAc%3DIIxDW6KiE03Mug9kArQsVTgZuoCnITjwhJShfNGHSDqKcV9J3I"
# api_key = "NSqahspwhsvva60OiwhsCGFhsyjECwMYD"
# api_secret ="bH3UY5CzrB1LWnIC51ngsgsghNk1zEALvFsj vjks7FNf4izFxLaf25PnNiGZD"
# client_id = "M0ZhTWt3elFIckp3Qfsns48u4bm5OWlI6MTpjaQ"
# client_secret = "qoFciMpVz_DX29DXKsjfigjHUFHUSshsmmkskngXwdEhx39p0ptClIJATq_F1Jjfb"  ----------------------------------$manipulated (dont use this one)

client = tweepy.Client(bearer_token,api_key,api_secret,access_token,access_token_secret)
auth= tweepy.OAuth1UserHandler(api_key,api_secret,access_token,access_token_secret)
api= tweepy.API(auth)

while(1):

    tweet_text = input("Enter your tweet: ")

    client.create_tweet(text = tweet_text)
 
