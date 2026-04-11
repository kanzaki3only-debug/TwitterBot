import tweepy
import os
import random

# =========================
# 🔐 환경변수 불러오기
# =========================
api_key = os.environ.get("API_KEY")
api_secret = os.environ.get("API_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_secret = os.environ.get("ACCESS_SECRET")
bearer_token = os.environ.get("BEARER_TOKEN")

# =========================
# 🧪 환경변수 체크 (디버깅용)
# =========================
if not all([api_key, api_secret, access_token, access_secret, bearer_token]):
    raise Exception("❌ API 키가 하나 이상 없습니다. GitHub Secrets 확인하세요.")

# =========================
# 🐦 Tweepy Client 생성
# =========================
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_secret
)

# =========================
# 📄 트윗 내용 불러오기
# =========================
with open("lines.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

if not lines:
    raise Exception("❌ lines.txt가 비어있습니다.")

tweet_text = random.choice(lines).strip()

print("📝 선택된 트윗:", tweet_text)

# =========================
# 🚀 트윗 보내기
# =========================
try:
    response = client.create_tweet(text=tweet_text)
    
    print("✅ SUCCESS: 트윗 전송 완료")
    print("📦 RESPONSE:", response.data)

except Exception as e:
    print("❌ ERROR 발생")
    print("타입:", type(e))
    print("내용:", e)
