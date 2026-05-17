def load_captions(filename):

    mapping = {}

    with open(filename, 'r', encoding='utf-8') as file:

        for line in file:

            tokens = line.strip().split('\t')

            if len(tokens) < 2:
                continue

            image_id, caption = tokens

            image_id = image_id.split('#')[0]

            caption = caption.lower()

            caption = "startseq " + caption + " endseq"

            if image_id not in mapping:
                mapping[image_id] = []

            mapping[image_id].append(caption)

    return mapping

def load_image_list(filename):

    with open(filename, 'r') as file:

        images = file.read().splitlines()

    return images