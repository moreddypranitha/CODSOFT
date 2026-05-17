import pickle
import numpy as np

from tensorflow.keras.models import load_model

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array

from tensorflow.keras.applications.resnet50 import preprocess_input

from src.feature_extractor import model

from src.caption_generator import generate_caption

# Enter image path
image_path = input("Enter image path: ")

# Load image
image = load_img(
    image_path,
    target_size=(224, 224)
)

# Convert image to array
image = img_to_array(image)

# Expand dimensions
image = np.expand_dims(image, axis=0)

# Preprocess image
image = preprocess_input(image)

# Extract features
feature = model.predict(image, verbose=0)

# Load trained model (.keras format)
caption_model = load_model(
    "models/caption_model.keras",
    compile=False
)

# Load tokenizer
with open(
    "dataset/processed/tokenizer.pkl",
    "rb"
) as f:

    tokenizer = pickle.load(f)

# Load max length
with open(
    "dataset/processed/max_length.pkl",
    "rb"
) as f:

    max_len = pickle.load(f)

# Generate caption
caption = generate_caption(
    caption_model,
    tokenizer,
    feature,
    max_len
)

print("\nGenerated Caption:")
print(caption)