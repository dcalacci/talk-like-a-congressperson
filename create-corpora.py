import pandas as pd
import numpy as np
import os

statements = pd.read_csv('static/fun_statements_subset.csv')

vocab = [word for word in open('static/vocab.txt', 'rb').readline().split()]

gb = statements.groupby('author_id')

num_authors = len(gb.groups.keys())
count = 0
for author_id, group in gb:
    count += 1
    print "processing text for author id #", author_id
    print "author #", count, " /", num_authors
    corpus_path = os.path.join('corpora/' + str(author_id).split('.')[0] + '/')

    if not os.path.exists(os.path.dirname(corpus_path)):
        print "path does not exist for author, creating path..."
        os.makedirs(os.path.dirname(corpus_path))


        count_2 = 0
        for n, row in group.iterrows():
            count_2 += 1
            if count_2 % 10 == 0:
                print "analyzed ", float(count_2)/len(group) * 100, "% of statements for author #", author_id
            text = row['cleaned_statement']
            words = text.split()

            out = open(os.path.join(corpus_path, 'corpus.txt'), 'a')

            for word in words:
                out.write(str(vocab.index(word)) + ' ')
            out.write('\n')
            out.close()
