from tensorflow.keras.preprocessing.text import Tokenizer

def create_tokenizer(captions):

    all_captions = []

    for key in captions:
        all_captions.extend(captions[key])

    tokenizer = Tokenizer()

    tokenizer.fit_on_texts(all_captions)

    return tokenizer

def max_length(captions):

    return max(
        len(caption.split())
        for caps in captions.values()
        for caption in caps
    )