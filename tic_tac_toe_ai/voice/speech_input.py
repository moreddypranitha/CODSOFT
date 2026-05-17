import speech_recognition as sr

def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Speak...")

        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)

        return text.lower()

    except:
        return ""