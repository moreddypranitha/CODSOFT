import os
import sys
import pickle
import numpy as np

# Add project root directory
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..'
        )
    )
)

from flask import Flask
from flask import render_template
from flask import request

from tensorflow.keras.models import load_model

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array

from tensorflow.keras.applications.resnet50 import preprocess_input

from src.feature_extractor import model
from src.caption_generator import generate_caption

app = Flask(__name__)

UPLOAD_FOLDER = 'web_app/static/uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load trained model
caption_model = load_model(
    'models/caption_model.keras',
    compile=False
)

# Load tokenizer
with open(
    'dataset/processed/tokenizer.pkl',
    'rb'
) as f:

    tokenizer = pickle.load(f)

# Load max length
with open(
    'dataset/processed/max_length.pkl',
    'rb'
) as f:

    max_len = pickle.load(f)


def predict_caption(image_path):

    # Load image
    image = load_img(
        image_path,
        target_size=(224, 224)
    )

    # Convert image to array
    image = img_to_array(image)

    # Expand dimensions
    image = np.expand_dims(
        image,
        axis=0
    )

    # Preprocess image
    image = preprocess_input(image)

    # Extract features
    feature = model.predict(
        image,
        verbose=0
    )

    # Generate caption
    caption = generate_caption(
        caption_model,
        tokenizer,
        feature,
        max_len
    )

    return caption


@app.route('/', methods=['GET', 'POST'])
def home():

    caption = None
    image_file = None

    if request.method == 'POST':

        file = request.files['image']

        if file:

            image_path = os.path.join(
                app.config['UPLOAD_FOLDER'],
                file.filename
            )

            # Save uploaded image
            file.save(image_path)

            # Generate caption
            caption = predict_caption(
                image_path
            )

            image_file = file.filename

    return render_template(
        'index.html',
        caption=caption,
        image_file=image_file
    )


if __name__ == '__main__':

    app.run(
        debug=True
    )