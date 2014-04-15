import random


class Markov:

    def __init__(self, corpus, n=3):
        self.corpus = corpus
        self.distribution = {}
        self.n = n
        self.populate_distribution()
        self.words = []
        [self.words.extend(d.words) for d in self.corpus.docs]

    def n_grams(self):
        """
        generates n-grams from this model's corpora.
        """
        for d in self.corpus.docs:
            doc_words = d.words

            if len(doc_words) < self.n:
                continue

            for i in range(len(doc_words) - (self.n)):
                yield tuple(doc_words[i:i+(self.n)])

    def populate_distribution(self):
        for tokens in self.n_grams():
            last_word = tokens[-1]
            key = tokens[:-1]
            if key in self.distribution:
                self.distribution[key].append(tokens[-1])
            else:
                self.distribution[key] = [last_word]

    def generate(self, length=30):
        seed = random.choice(self.distribution.keys())
        phrase = seed + (self.distribution[seed][0],)

        generated = []

        for i in xrange(length):
            generated.append(phrase[0])
            key = tuple(phrase[1:])
            if key in self.distribution.keys():
                # pick a word if we have a history
                next = random.choice(self.distribution[tuple(phrase[1:])])
            else:
                # otherwise, it's a uniform distribution
                next = random.choice(self.words)
            phrase = phrase[1:] + (next,)

        generated.append(phrase[0])

        return " ".join([self.corpus.vocab[int(i)] for i in generated])
