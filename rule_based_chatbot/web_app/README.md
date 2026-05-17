# Rule-Based Voice Chatbot

A simple AI-powered Rule-Based Chatbot built using Python, Flask, HTML, CSS, and JavaScript.

The chatbot supports:
- Text chat
- Voice input using microphone
- Rule-based responses
- Modern web interface
- Speech recognition

---

# Features

- Rule-based chatbot responses
- Voice recognition using browser microphone
- Flask web application
- Beautiful responsive UI
- Chat logging support
- GUI chatbot support
- Voice chatbot support
- Beginner-friendly project structure

---

# Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Speech Recognition API

---

# Project Structure

```bash
rule_based_chatbot/
│
├── chatbot.py
├── responses.py
├── requirements.txt
├── README.md
│
├── logs/
│   └── chat_logs.txt
│
├── gui/
│   └── gui_chatbot.py
│
├── voice_bot/
│   └── voice_chatbot.py
│
├── web_app/
│   ├── app.py
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   └── static/
│       ├── style.css
│       └── script.js
│
└── advanced/
    └── pattern_chatbot.py
```

---

# Installation

## Step 1: Clone Repository

```bash
git clone <repository_link>
```

OR download ZIP manually.

---

## Step 2: Open Project

Open project folder in:

- Visual Studio Code

---

## Step 3: Install Required Libraries

```bash
pip install flask speechrecognition pyttsx3 pyaudio nltk
```

---

# How to Run

## Run Console Chatbot

```bash
python chatbot.py
```

---

## Run GUI Chatbot

```bash
python gui/gui_chatbot.py
```

---

## Run Voice Chatbot

```bash
python voice_bot/voice_chatbot.py
```

---

## Run Web Voice Chatbot

```bash
python web_app/app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

# Voice Recognition Setup

## Allow Browser Microphone Permission

When browser asks:

```text
Allow microphone access?
```

Click:

```text
Allow
```

---

# Browser Support

Recommended browsers:

- Google Chrome
- Microsoft Edge

---

# Example Inputs

```text
hello
what is your name
how are you
bye
```

---

# Example Responses

```text
Hello!
I am a Rule-Based Chatbot.
I am doing great!
Goodbye!
```

---

# Chat Logging

Chat conversations are stored in:

```text
logs/chat_logs.txt
```

---

# Future Enhancements

- AI-powered chatbot
- NLP integration
- Database support
- User authentication
- Multi-language support
- Voice output
- Chat history
- Dark mode
- Mobile responsive UI
- OpenAI/Gemini integration
- Emotion detection
- Hospital assistant integration

---

# Future Upgrade Ideas

## Beginner Level
- Add more chatbot responses
- Improve UI
- Add chatbot avatar

## Intermediate Level
- SQLite database
- User accounts
- Conversation memory

## Advanced Level
- Machine Learning chatbot
- Deep Learning NLP
- Voice assistant
- Real-time AI chatbot
- Hospital navigation assistant

---

# Troubleshooting

## Flask Error

```text
ModuleNotFoundError: No module named 'flask'
```

Solution:

```bash
pip install flask
```

---

## Voice Recognition Error

```text
Error: not-allowed
```

Solution:
- Allow microphone permission in browser
- Use Google Chrome

---

## Microphone Not Working

- Enable microphone access in Windows settings
- Restart browser

---

# License

This project is for educational purposes.

---

# Author

Developed using Python and Flask for learning chatbot development.