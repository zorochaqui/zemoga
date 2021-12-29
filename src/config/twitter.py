import tweepy
from dotenv import load_dotenv
import os
load_dotenv()

def twitter():
    TWITTER_API_KEY             = os.getenv("TWITTER_API_KEY")
    TWITTER_API_SECRET_KEY      = os.getenv("TWITTER_API_SECRET_KEY")
    TWITTER_ACCESS_TOKEN        = os.getenv("TWITTER_ACCESS_TOKEN")
    TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    
    return api