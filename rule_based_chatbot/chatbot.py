from responses import get_response
from database.db import create_database, save_chat

create_database()

print("===================================")
print(" Rule-Based Chatbot ")
print(" Type 'bye' to exit ")
print("===================================")

while True:

    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Bot: Goodbye!")
        break

    response = get_response(user_input)

    print("Bot:", response)

    save_chat(user_input, response)

    with open("logs/chat_logs.txt", "a") as file:
        file.write(f"You: {user_input}\n")
        file.write(f"Bot: {response}\n\n")