from Model import get_client, get_model, get_system_prompt
from TextToSpeech import speak
from RealtimeSearchEngine import search
from datetime import datetime
from Automation import open_app, open_website, take_screenshot, volume_up, volume_down, mute
from SpeechToText import listen



chat_history = []
SEARCH_KEYWORDS = [
    "latest", "today", "news", "current", "who won", "AI",
    "live", "technology", "university", "update","syllabus",
    "weather", "price", "score", "2025", "2026", "recently",
    "founder", "who is", "who was", "when did", "what is"
]

def needs_search(message):
    message_lower = message.lower()
    return any(keyword in message_lower for keyword in SEARCH_KEYWORDS)

def chat(user_message):
    msg = user_message.lower()

    if "time" in msg:
        return f"The current time is {datetime.now().strftime('%I:%M %p')}"
    if "date" in msg or "day" in msg:
        return f"Today is {datetime.now().strftime('%A,%B %d, %Y')}"

    if "open" in msg:
        if "youtube" in msg:
            return open_website("youtube")
        elif "google" in msg:
            return open_website("google")
        elif "facebook" in msg:
            return open_website("facebook")
        elif "instagram" in msg:
            return open_website("instagram")
        elif "notepad" in msg:
            return open_app("notepad")
        elif "calculator" in msg:
            return open_app("calculator")

    if "screenshot" in msg:
        return take_screenshot()
    if "volume up" in msg:
        return volume_up()
    if "volume down" in msg:
        return volume_down()
    if "mute" in msg:
        return mute()

    chat_history.append({"role": "user", "content": user_message})

    if needs_search(user_message):
        search_result = search(user_message)
        user_message = f"{user_message}\n\nSearch Results: {search_result}"

    messages = [{"role": "system", "content": get_system_prompt()}] + chat_history
    client = get_client()
    response = client.chat.completions.create(
        model=get_model(),
        messages=messages,
        max_tokens=1024,
        temperature=0.7
    )
    reply = response.choices[0].message.content
    chat_history.append({"role": "assistant", "content": reply})
    return reply

def clear_history():
    chat_history.clear()

def get_history():
    return chat_history

if __name__ == "__main__":
    print("Jarvis Started!")
    while True:
        print("Speak to Jarvis...")
        user_input = input("You: ")
        if not user_input:
            continue
        print(f"You: {user_input}")
        if user_input.lower() == "quit":
            print("Jarvis: Goodbye sir!")
            speak("Goodbye sir!")
            break
        response = chat(user_input)
        print(f"Jarvis: {response}\n")
