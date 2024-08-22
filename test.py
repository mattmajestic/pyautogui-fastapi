import requests

url = "http://127.0.0.1:8000/twitch_chat_action/"

# Parameters for the API
payload = {
    "chatbox_coords": (1271, 963),   # Coordinates for the chatbox
    "message": "Hello from PyAutoGUI",  # Message to type
    "emoji": "😊",   # Emoji to type
    "confirm_coords": (1543, 1004)  # Coordinates for the confirmation action
}

# Send the request
response = requests.post(url, json=payload)

# Print the response
print(response.json())
