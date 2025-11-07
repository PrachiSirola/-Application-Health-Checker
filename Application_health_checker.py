import requests
import time
from datetime import datetime
apps = {
    "Google": "https://www.google.com",
    "YouTube": "https://www.youtube.com",
    "GitHub": "https://www.github.com",
    "Wikipedia": "https://www.wikipedia.org",
    "Reddit": "https://www.reddit.com"
}
wait_in_sec = 40 
xxx = "app_health_log.txt"  
def abc(msg):
    with open(xxx, "a", encoding="utf-8") as f:
        f.write(msg + "\n")

while True:
    c_time = datetime.now().strftime("Date: %d-%m-%Y || Time: %H:%M:%S")
    print("APP HEALTH CHECKER")
    print(c_time)
    for name, url in apps.items():
        try:
            ans = requests.get(url, timeout=5)
            rtime = ans.elapsed.total_seconds()  
            if ans.status_code == 200:
                msg = f"{name} is up (Status: {ans.status_code}, Response time: {rtime:.2f}s)"
            else:
                msg = f"{name} returned error (Status: {ans.status_code}, Response time: {rtime:.2f}s)"
        except requests.exceptions.RequestException:
            msg = f"{name} is down (No response)"
        print(msg)
        abc(msg)
    print("END .............................................")
    time.sleep(wait_in_sec)
