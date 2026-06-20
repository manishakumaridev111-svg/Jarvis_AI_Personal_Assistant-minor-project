import speech_recognition as sr

recognizer = sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError:
        print("Speech service unavailable")
        return ""


if __name__ == "__main__":
    result = listen()
    print(f"Result: {result}")