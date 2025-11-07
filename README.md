# -Application-Health-Checker
A simple Python script that monitors the uptime of web applications by checking their HTTP status codes.
It reports whether each application is UP (functioning correctly) or DOWN (not responding/unavailable) and logs the results to a file.
# Features
- Checks multiple websites or apps at regular intervals
- Detects if an app is up or down using HTTP status codes
- Logs every check with timestamps and response times
- Simple and lightweight — no external monitoring tools needed
# How it Works 
- The script sends HTTP requests to each listed application.
- It checks the response status code:
  200 → App is UP
- Any other code or timeout → App is DOWN
- Logs results to a text file (app_health_log.txt) along with date, time, and response time.
- Repeats the check every 40 seconds (customizable).
# Requirements
- Python 3.x
- requests library
  Install dependencies:
  ```bash
  pip install requests
  ```
# Usage
- Clone this repository:
```bash
git clone https://github.com/prachisirola/-Application-Health-Checker.git
cd application-uptime-checker
```
- Run the script:
```bash
python project_code.py
```
- Check the log file for uptime history:
```bash
app_health_log.txt
```
# Configuration
You can edit the script to:
- Add or remove URLs inside the apps dictionary
- Change the interval time (wait_in_sec) as needed
- # Example Output
```bash
APP HEALTH CHECKER
Date: 07-11-2025 || Time: 11:25:43
Google is up (Status: 200, Response time: 0.12s)
YouTube is up (Status: 200, Response time: 0.25s)
Reddit is down (No response)
END .............................................
```
