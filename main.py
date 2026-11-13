
import os
import requests

webhook = os.environ.get("DISCORD_WEBHOOK")

if not webhook:
    raise ValueError("Discord webhook is missing!")

response = requests.post(
    webhook,
    json={"content": "✅ TAMO Discord Bot successfully connected!"}
)

response.raise_for_status()
print("Discord connection successful!")
