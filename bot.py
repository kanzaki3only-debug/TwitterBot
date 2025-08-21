import tweepy
import os
import random

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

# lines.txt에서 문장 불러오기
with open("lines.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 랜덤으로 하나 선택
tweet_text = random.choice(lines).strip()

# 트윗 작성
try:
    response = client.create_tweet(text=tweet_text)
    print("✅ Tweet successful:", response)
except Exception as e:
    print("❌ Error:", e)
