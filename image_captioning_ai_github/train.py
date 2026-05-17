import pickle

from src.dataset_loader import load_captions
from src.dataset_loader import load_image_list

from src.feature_extractor import extract_features
from src.feature_extractor import save_features

from src.tokenizer_utils import create_tokenizer
from src.tokenizer_utils import max_length

from src.model_builder import build_model

from src.sequence_generator import create_sequences

# Dataset paths
captions_path = "dataset/Flickr8k_text/Flickr8k.token.txt"

train_images_path = (
    "dataset/Flickr8k_text/Flickr_8k.trainImages.txt"
)

images_dir = "dataset/Flickr8k_Dataset"

print("Loading captions...")

captions = load_captions(captions_path)

print("Loading training image list...")

# Use only 200 images for faster training
train_images = load_image_list(
    train_images_path
)[:200]

# Filter captions
filtered_captions = {
    image: captions[image]
    for image in train_images
}

print("Extracting image features...")

features = extract_features(
    images_dir,
    train_images
)

# Save extracted features
save_features(
    features,
    "dataset/processed/features.pkl"
)

print("Creating tokenizer...")

tokenizer = create_tokenizer(
    filtered_captions
)

vocab_size = len(
    tokenizer.word_index
) + 1

max_len = max_length(
    filtered_captions
)

# Save tokenizer
with open(
    "dataset/processed/tokenizer.pkl",
    "wb"
) as f:

    pickle.dump(tokenizer, f)

# Save max length
with open(
    "dataset/processed/max_length.pkl",
    "wb"
) as f:

    pickle.dump(max_len, f)

print("Preparing sequences...")

X1, X2, y = create_sequences(
    tokenizer,
    max_len,
    filtered_captions,
    features,
    vocab_size
)

print("Building model...")

model = build_model(
    vocab_size,
    max_len
)

print("Training model...")

model.fit(
    [X1, X2],
    y,
    epochs=2,
    batch_size=32,
    verbose=1
)

# Save model in new Keras format
model.save(
    "models/caption_model.keras"
)

print("\nTraining completed successfully!")
print("Model saved as:")
print("models/caption_model.keras")