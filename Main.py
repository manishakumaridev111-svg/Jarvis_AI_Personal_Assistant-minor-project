from Backend.chatbot  import chat
from Backend.TextToSpeech import speak
from Backend.RealtimeSearchEngine import search
from Backend.SpeechToText import listen 


print("Jarvis Started")
speak("Hello Master")  # Test if this speaks

while True:
    query = input("You : ")

    response = reply(query)

    print("Jarvis :", response)
    print("Calling speak now...")  # ← add this
    #speak(response)

