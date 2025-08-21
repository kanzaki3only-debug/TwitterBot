import os
import sys
import random
import tweepy
from dotenv import load_dotenv

# .env 불러오기
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_KEY_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_SECRET")

# 트위터 인증
auth = tweepy.OAuth1UserHandler(
    API_KEY,
    API_KEY_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)

# 대사 불러오기
with open("lines.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

# 랜덤으로 한 줄 선택
tweet_text = random.choice(lines)

# 트윗 발행
try:
    tweet = api.update_status(tweet_text)
    print(f"✅ 트윗 성공! ID: {tweet.id} / 내용: {tweet_text}")
except Exception as e:
    print("[오류] 트윗 실패:", e)

