import requests

def send_line_notify(message, token):
    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"message": message}

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        print("Notification sent successfully!")
    else:
        print(f"Failed to send notification. Status code: {response.status_code}")
        print(response.text)

# Replace 'YOUR_TOKEN_HERE' with the actual token you obtained
line_notify_token = 'f0L5QtMvXIYNFMnS2SwhZ7E4fFNGJvquZ3kWk2bz9ob'

# Replace 'Hello, Line Notify!' with the message you want to send
message_to_send = 'Hello, Line Notify!'

send_line_notify(message_to_send, line_notify_token)
