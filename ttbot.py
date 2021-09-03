#!/usr/bin/env python3

import tweepy

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

timeline = api.home_timeline()

for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")


#f = open("audiorecording.txt", "r")
#texto_arquivo = f.read()
api.update_status("testing before uploading to github! go see my source code on https://github.com/Kevinlinuxapprentice/caleb")
