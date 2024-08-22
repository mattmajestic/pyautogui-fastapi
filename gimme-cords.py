import pyautogui
import keyboard

print("Hover over the desired location and press 'Enter' to get the coordinates.")
print("Press 'Esc' to exit the program.")

while True:
    try:
        # If Enter is pressed, capture and print the coordinates
        if keyboard.is_pressed('enter'):
            x, y = pyautogui.position()
            print(f"Mouse position captured: ({x}, {y})")
            keyboard.wait('enter')  # Wait to release the Enter key before continuing

        # If Esc is pressed, exit the loop
        if keyboard.is_pressed('esc'):
            print("Exiting...")
            break

    except Exception as e:
        print(f"An error occurred: {e}")
        break
