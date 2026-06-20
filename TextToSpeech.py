import pyttsx3
import threading
import queue

_queue = queue.Queue()

def _worker():
    print("Worker started")
    import pythoncom
    pythoncom.CoInitialize()
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 175)

    while True:
        text = _queue.get()
        if text is None:
            break

        #Split long text into sentences
        sentences = text.replace('!','.').split('.')
        for sentence in sentences:
            if sentence.strip():
                print("Speaking: " , sentence)
                engine.say(sentence)
        engine.runAndWait()


_thread = threading.Thread(target=_worker, daemon=True)
_thread.start()

def speak(text):
    print("Speak called: " , text[:50])
    if text and text.strip():
        while not _queue.empty():
            try:
                _queue.get_nowait()
            except:
                pass
        _queue.put(text)

def set_voice(gender="male"):
    pass

def set_rate(rate=175):
    pass
