import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from responses import get_response

def send_message():

    user_message = entry.get()

    chat_window.insert(tk.END, "You: " + user_message + "\n")

    response = get_response(user_message.lower())

    chat_window.insert(tk.END, "Bot: " + response + "\n\n")

    entry.delete(0, tk.END)

root = tk.Tk()

root.title("GUI Chatbot")

chat_window = tk.Text(root, width=50, height=20)
chat_window.pack()

entry = tk.Entry(root, width=40)
entry.pack()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()