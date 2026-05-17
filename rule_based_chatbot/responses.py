import datetime
import random
import re

def get_response(user_input):

    greetings = ["hello", "hi", "hey"]

    if any(word in user_input for word in greetings):
        return random.choice([
            "Hello!",
            "Hi there!",
            "Hey!"
        ])

    elif re.search(r'how are you', user_input):
        return "I am fine."

    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"Current time is {current_time}"

    elif "date" in user_input:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        return f"Today's date is {current_date}"

    elif "your name" in user_input:
        return "I am a Rule-Based Chatbot."

    else:
        return "Sorry, I don't understand."