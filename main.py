from fastapi import FastAPI, HTTPException
import pyautogui

app = FastAPI()

@app.post("/twitch_chat_action/")
def twitch_chat_action(
    chatbox_coords: tuple[int, int] = (1271, 963),
    message: str = "Hello from PyAutoGUI",
    emoji: str = "😊",
    confirm_coords: tuple[int, int] = (1543, 1004)
):
    try:
        # Move to chatbox and click
        pyautogui.moveTo(chatbox_coords[0], chatbox_coords[1])
        pyautogui.click()
        
        # Type the message
        pyautogui.write(message)
        pyautogui.press('enter')
        
        # Type the emoji
        pyautogui.write(emoji)
        pyautogui.press('enter')
        
        # Move to confirm button and click
        pyautogui.moveTo(confirm_coords[0], confirm_coords[1])
        pyautogui.click()
        
        return {
            "message": "Action completed successfully",
            "chatbox_coords": chatbox_coords,
            "typed_message": message,
            "typed_emoji": emoji,
            "confirm_coords": confirm_coords
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
