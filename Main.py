from Backend.Model  import reply
from Backend.TextToSpeech import speak

print("Jarvis Started")
speak("Hello Master")  # Test if this speaks

while True:
    query = input("You : ")

    response = reply(query)

    print("Jarvis :", response)
    print("Calling speak now...")  # ← add this
    #speak(response)

