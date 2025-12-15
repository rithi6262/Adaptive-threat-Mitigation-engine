import requests
import time

URL = "http://127.0.0.1:5000/login"

username = "shruti"          # ✅ change to shruti
wrong_password = "wrongpass" # any wrong password

attempts = 12                # do 10–15 attempts
delay_sec = 0.2              # small delay to look "real"

for i in range(attempts):
    try:
        r = requests.post(
            URL,
            data={"username": username, "password": wrong_password},
            allow_redirects=False  # keeps it fast
        )
        print(f"Attempt {i+1}/{attempts} -> HTTP {r.status_code}")
    except Exception as e:
        print("Request failed:", e)
    time.sleep(delay_sec)