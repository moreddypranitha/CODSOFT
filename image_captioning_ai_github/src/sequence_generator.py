import numpy as np

from tensorflow.keras.preprocessing.sequence import pad_sequences

from tensorflow.keras.utils import to_categorical

def create_sequences(
    tokenizer,
    max_len,
    captions,
    features,
    vocab_size
):

    X1, X2, y = list(), list(), list()

    for image_id, caps in captions.items():

        feature = features[image_id]

        for caption in caps:

            seq = tokenizer.texts_to_sequences([caption])[0]

            for i in range(1, len(seq)):

                in_seq = seq[:i]

                out_seq = seq[i]

                in_seq = pad_sequences(
                    [in_seq],
                    maxlen=max_len
                )[0]

                out_seq = to_categorical(
                    [out_seq],
                    num_classes=vocab_size
                )[0]

                X1.append(feature)
                X2.append(in_seq)
                y.append(out_seq)

    return (
        np.array(X1),
        np.array(X2),
        np.array(y)
    )