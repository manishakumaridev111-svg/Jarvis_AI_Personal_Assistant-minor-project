import os
import subprocess
import webbrowser
import pyautogui
from datetime import datetime

def open_app(app_name):
    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "chrome": "chrome.exe",
        "paint": "mspaint.exe",
        "word": "winword.exe",
        "excel": "excel.exe",
        "task manager": "taskmgr.exe",
        "file explorer": "explorer.exe"
    }
    app = apps.get(app_name.lower())
    if app:
        subprocess.Popen(app)
        return f"Opening {app_name}"
    return f"App {app_name} not found"

def open_website(url):
    import webbrowser
    sites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "facebook": "https://www.facebook.com",
        "instagram": "https://www.instagram.com"
    }
    for site, link in sites.items():
        if site in url.lower():
            webbrowser.open(link)
            return f"Opening {site}"
    webbrowser.open(f"https://www.{url}.com")
    return f"Opening {url}"


def take_screenshot():
    filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    return f"Screenshot saved as {filename}"

def shutdown():
    os.system("shutdown /s /t 5")
    return "Shutting down in 5 seconds!"

def restart():
    os.system("shutdown /r /t 5")
    return "Restarting in 5 seconds!"

def volume_up():
    for _ in range(5):
        pyautogui.press("volumeup")
    return "Volume increased"

def volume_down():
    for _ in range(5):
        pyautogui.press("volumedown")
    return "Volume decreased"

def mute():
    pyautogui.press("volumemute")
    return "Volume muted"
if __name__ == "__main__":
    print(open_website("youtube"))