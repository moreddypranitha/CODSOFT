import sys
import os

# Add parent folder path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import speech_recognition as sr
import pyttsx3
from responses import get_response

# Initialize recognizer
recognizer = sr.Recognizer()

# Initialize voice engine
engine = pyttsx3.init()

# Voice speed
engine.setProperty('rate', 150)

print("===================================")
print(" Voice Chatbot Started ")
print(" Say 'bye' to exit ")
print("===================================")

while True:

    try:
        with sr.Microphone() as source:

            print("\nListening...")

            # Reduce noise
            recognizer.adjust_for_ambient_noise(source, duration=1)

            # Listen
            audio = recognizer.listen(source)

            print("Recognizing...")

            # Convert speech to text
            text = recognizer.recognize_google(audio)

            # SHOW USER VOICE INPUT
            print("You said:", text)

            # Exit condition
            if text.lower() == "bye":

                response = "Goodbye!"

                print("Bot:", response)

                engine.say(response)
                engine.runAndWait()

                break

            # Get chatbot response
            response = get_response(text.lower())

            # SHOW BOT RESPONSE
            print("Bot:", response)

            # Speak response
            engine.say(response)
            engine.runAndWait()

    except sr.UnknownValueError:

        print("Could not understand audio")

    except sr.RequestError:

        print("Internet connection issue")

    except Exception as e:

        print("Error:", e)