import numpy as np

from tensorflow.keras.preprocessing.sequence import pad_sequences

def generate_caption(
    model,
    tokenizer,
    photo,
    max_len
):

    in_text = 'startseq'

    for i in range(max_len):

        sequence = tokenizer.texts_to_sequences(
            [in_text]
        )[0]

        sequence = pad_sequences(
            [sequence],
            maxlen=max_len
        )

        yhat = model.predict(
            [photo, sequence],
            verbose=0
        )

        yhat = np.argmax(yhat)

        word = tokenizer.index_word.get(yhat)

        if word is None:
            break

        in_text += ' ' + word

        if word == 'endseq':
            break

    return in_text.replace(
        'startseq',
        ''
    ).replace(
        'endseq',
        ''
    ).strip()