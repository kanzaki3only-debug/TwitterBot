import tweepy
import os

# 환경변수에서 키 불러오기
api_key = os.environ["API_KEY"]
api_secret = os.environ["API_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_secret = os.environ["ACCESS_SECRET"]

# Tweepy Client (Twitter API v2)
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_secret
)

# 트윗 작성
try:
    response = client.create_tweet(text="Hello from Twitter API v2 🐦")
    print("✅ Tweet successful:", response)
except Exception as e:
    print("❌ Error:", e)
