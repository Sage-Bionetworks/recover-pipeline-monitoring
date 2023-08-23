import requests
import json
import sys

def send_slack_message(payload, webhook):
    """Send a Slack message to a channel via a webhook. 
    
    Args:
        payload (dict): Dictionary containing Slack message, i.e. {"text": "This is a test"}
        webhook (str): Full Slack webhook URL for your chosen channel. 
    
    Returns:
        HTTP response code, i.e. <Response [503]>
    """

    return requests.post(webhook, json.dumps(payload))

# Check if the script is being run with the correct number of arguments
if len(sys.argv) != 3:
    print("Usage: python send_slack.py <payload_json> <webhook_url>")
    sys.exit(1)

# Parse command-line arguments
payload_json = sys.argv[1]
webhook_url = sys.argv[2]

# Convert the JSON string argument to a Python dictionary
payload = json.loads(payload_json)

# Call the send_slack_message function with the provided arguments
response = send_slack_message(payload, webhook_url)
print("HTTP response:", response)
