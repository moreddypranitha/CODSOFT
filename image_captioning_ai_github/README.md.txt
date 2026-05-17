# Image Captioning AI

An AI-powered Image Captioning system built using Deep Learning, Computer Vision, and Natural Language Processing.

This project uses:

- ResNet50 for image feature extraction
- LSTM for caption generation
- TensorFlow/Keras for model training
- Flask for frontend deployment

---

# Features

- Upload image through web interface
- Generate AI captions automatically
- Deep Learning based caption generation
- Flickr8k dataset support
- Modern Flask frontend
- TensorFlow + Keras integration

---

# Project Structure

image_captioning_ai/
│
├── train.py
├── predict.py
├── requirements.txt
├── README.md
│
├── dataset/
│   ├── Flickr8k_Dataset/
│   ├── Flickr8k_text/
│   └── processed/
│
├── models/
│   └── caption_model.keras
│
├── src/
│   ├── __init__.py
│   ├── dataset_loader.py
│   ├── feature_extractor.py
│   ├── tokenizer_utils.py
│   ├── model_builder.py
│   ├── sequence_generator.py
│   ├── caption_generator.py
│   └── utils.py
│
└── web_app/
    ├── app.py
    │
    ├── templates/
    │   └── index.html
    │
    └── static/
        ├── style.css
        └── uploads/

---

# Dataset

Dataset Used:
Flickr8k Dataset

Kaggle Link:
https://www.kaggle.com/datasets/sayanf/flickr8k

Download and place:

- Flickr8k_Dataset
- Flickr8k_text

inside:

dataset/

---

# Installation

## Clone Project

git clone <repository_url>

---

## Open Project

Open the folder in VS Code.

---

## Install Libraries

pip install -r requirements.txt

---

# Train Model

Run:

python train.py

After training completes:

models/caption_model.keras

will be created.

---

# Predict Captions

Run:

python predict.py

Enter image path:

dataset/Flickr8k_Dataset/1000268201_693b08cb0e.jpg

---

# Run Flask Frontend

From main project folder:

python web_app/app.py

Open browser:

http://127.0.0.1:5000

---

# Technologies Used

- Python
- TensorFlow
- Keras
- Flask
- NumPy
- ResNet50
- LSTM
- NLP

---

# Future Enhancements

- Transformer-based captioning
- Attention mechanism
- Voice output
- Real-time webcam captioning
- BLEU score evaluation
- Beam search decoding
- Mobile app deployment
- Cloud deployment

---

# Sample Output

Generated Caption:

a man in a blue shirt standing outside

---

# Author

Developed as an AI Image Captioning Project using Deep Learning and NLP.
