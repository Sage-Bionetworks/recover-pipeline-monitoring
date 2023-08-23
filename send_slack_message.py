import requests
import sys

webhook_url = "https://hooks.slack.com/services/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"

def send_slack_message(message):
    payload = {
        "text": message
    }
    response = requests.post(webhook_url, json=payload)
    if response.status_code != 200:
        print("Error sending Slack message")
        sys.exit(1)

send_slack_message("Cron job started")
