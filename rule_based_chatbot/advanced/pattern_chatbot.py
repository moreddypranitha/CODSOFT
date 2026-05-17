import re

while True:

    text = input("You: ").lower()

    if text == "bye":
        print("Bot: Goodbye!")
        break

    elif re.search(r'hello|hi|hey', text):
        print("Bot: Hello!")

    elif re.search(r'how are you', text):
        print("Bot: I am fine.")

    else:
        print("Bot: Sorry, I don't understand.")