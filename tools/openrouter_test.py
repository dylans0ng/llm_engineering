"""Simple helper to test OpenRouter API key and list models.
Run: python tools/openrouter_test.py
"""
import os
from dotenv import load_dotenv
import requests
import pprint

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = "https://openrouter.ai/api/v1"

if not API_KEY:
    print("OPENROUTER_API_KEY not set. Copy .env.example to .env and set your key, or set environment variable.")
    raise SystemExit(1)

headers = {"Authorization": f"Bearer {API_KEY}"}
resp = requests.get(f"{BASE_URL}/models", headers=headers)
try:
    resp.raise_for_status()
except Exception as e:
    print("Request failed:", e)
    print("Status code:", resp.status_code)
    print(resp.text)
    raise

# pprint.pp(resp.json())
data = resp.json().get("data", [])
kimi_models = [m["id"] for m in data if "kimi" in m.get("id","").lower()]

if kimi_models:
    MODEL = kimi_models[0]   # choose first match
    print("Using model:", MODEL)
else:
    MODEL = "llama3.2:latest"  # fallback
    print("Kimi not found — using fallback:", MODEL)