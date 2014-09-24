import os
import re


class Document:
    def __init__(self):
        self.words = []
        self.length = 0


class Corpus:
    """
    each corpus must be its own file.
    the filename is the name of the corpus.
    each document is represented as a line in the corpus file.
    Each document is represented by a vector of integers.
    Each element of the vector corresponds to a unique identifier for a word,
    defined in a separate vocab file (to save memory).
    """

    def __init__(self, vocab, name="", docs=[], num_docs=0):
        self.name = name
        self.vocab = vocab
        self.vocab_size = len(vocab)
        self.docs = docs
        self.num_docs = num_docs


def read_data(corpus_path, vocab_path):
    print "looking for file at:", corpus_path
    if not os.path.exists(corpus_path):
        print "couldn't find file - try again!"
        return

    # each corpus is a file
    corpus_name = os.path.basename(corpus_path).split('.')[0]
    corpus_name = re.sub(corpus_name, "_", " ")

    print "looking for vocab at:", vocab_path
    # get vocab list
    vocab = [word for word in open(vocab_path, 'rb').read().split()]

    c = Corpus(vocab)
    c.name = corpus_name

    # each line is a document
    with open(corpus_path) as f:
        for line in f:
            d = Document()
            wordids = line.strip().split()
            d.words = wordids
            d.length = len(d.words)
            c.docs.append(d)
    return c
