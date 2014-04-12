# utilities for text transformation and stuff like that


def get_words_from_file(path):
    with open(path) as f:
        data = f.read()
        words = data.split()
    return words
