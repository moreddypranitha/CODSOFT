import os
import pickle
import numpy as np

from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.models import Model

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array

from tensorflow.keras.applications.resnet50 import preprocess_input

base_model = ResNet50(weights='imagenet')

model = Model(
    inputs=base_model.inputs,
    outputs=base_model.layers[-2].output
)

def extract_features(directory, image_list):

    features = {}

    for image_name in image_list:

        image_path = os.path.join(directory, image_name)

        image = load_img(
            image_path,
            target_size=(224, 224)
        )

        image = img_to_array(image)

        image = np.expand_dims(image, axis=0)

        image = preprocess_input(image)

        feature = model.predict(image, verbose=0)

        features[image_name] = feature[0]

        print("Processed:", image_name)

    return features

def save_features(features, filename):

    with open(filename, 'wb') as f:
        pickle.dump(features, f)
