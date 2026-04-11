import os
import tweepy
import random

# =========================
# 🔐 환경변수 불러오기
# =========================
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_SECRET")

# =========================
# ❗ 키 체크 (없으면 바로 에러)
# =========================
if not all([api_key, api_secret, access_token, access_secret]):
    raise Exception("❌ API 키가 하나 이상 없습니다. GitHub Secrets 확인하세요.")

# =========================
# 🔑 인증 (OAuth1)
# =========================
auth = tweepy.OAuth1UserHandler(
    api_key,
    api_secret,
    access_token,
    access_secret
)

api = tweepy.API(auth)

# =========================
# 📄 트윗 내용 불러오기
# =========================
with open("lines.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

if not lines:
    raise Exception("❌ lines.txt가 비어있습니다.")

tweet_text = random.choice(lines).strip()

print("📝 트윗 내용:", tweet_text)

# =========================
# 🚀 트윗 전송
# =========================
try:
    api.update_status(tweet_text)
    print("✅ 트윗 성공!")

except Exception as e:
    print("❌ 에러 발생")
    print(type(e))
    print(e)
