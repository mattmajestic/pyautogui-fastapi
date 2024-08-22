# 🚀 FastAPI + PyAutoGUI Twitch Chat Automation

This project is a simple FastAPI service that automates interaction with your Twitch chat using `PyAutoGUI`. 

## 📂 Files

- `main.py`: The FastAPI service that listens for requests and automates the Twitch chat interaction.
- `test.py`: A test script to send a request to the FastAPI service and automate the Twitch chat actions.

## ⚙️ How It Works

1. **Move the mouse** to the Twitch chatbox and click.
2. **Type a custom message** and press Enter.
3. **Type an emoji** and press Enter.
4. **Move the mouse** to a confirmation button and click.

## Get Started 

```
pip install -r requirements.txt
uvicorn main:app --reload
```

in another terminal you can test
```
python test.py
```