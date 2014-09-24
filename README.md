talk-like-a-congressman
=======================

http://talk-like-a-congressperson.dcalacci.net/

n-gram models trained on congressional public speech data.

I'm working with this data as part of the
[lazer lab](http://www.lazerlab.net) at Northeastern University, so I decided
to have a little fun with it.

## Usage

### Web

Install the requirements:

```
pip install -r requirements.txt
```

```
python talk-like-a-congressman.py
```
Then go to `http://127.0.0.1:5000`


### API (I guess?)
The URLs are nice enough that you can probably use this as an API, if you really want.
url format:

```
talk-like-a-congressperson.dcalacci.net/congressperson/<VoteSmart id>/generate/<ngram length>/<generated text length>
```

--
### Local

To run it on the command line, you have to use the python functions:

```python
import corpus
import markov
```

read the vocabulary data and the data of the congressman you want to talk like:

```python
c = corpus.read_data('corpora/1032/corpus.txt', 'vocab.txt')
```

create the markov model:

```python
m = markov.Markov(c, 3)
```

generate some text:

```python
m.generate(100)
```
should output something like:

```
they now have better access to technology in the affordable care
act is already paying dividends for millions of americans with more to
come children can no longer have the records to defend themselves
similarly at least some irs agents have taken the position that anyone
who claimed edc benefits as a certainly as a participant in a recent
report from the leaders and residents of the pre jobs act with respect
to the united states and that met the program s criteria for creating
jobs and economic opportunity for virgin islanders the increase of our
nation i believe the path'
```

or

```
their continued success we must find better ways to reward teacher
excellence and innovation expand access to more affordable as our
economy becomes increasingly necessary to enter the workforce
unfortunately rising tuition costs force the average borrower 17 500
into debt upon graduation a recent report from the national center for
disease control and epa to put train and deploy mixed teams depending
on the particular environment we ve got about a thousand people out of
their component either in a different direction the legislation before
both the house and senate authorizing committees the subcommittee that
is the way we work
```

No punctuation, just words. This is an artifact from how I generated
the corpus.

The script that takes the pandas dataframe I have with all the
statements in the dataset and converts it to the format needed for
this project literally takes days to complete, so making the generated
text better is really a matter of me running the script again.


## A little documentation

Each congresspersons' collection of public statements is considered a
separate corpus.

Each corpus consists of some number of documents, and each document
consists of some number of tokens, or words.

A corpus is represented as a single file, where each line is a
document. Each word is an integer, and words are separated by spaces.

There is a single `vocab.txt` file for all the corpora that serves to
map tokens to integer IDs.

`vocab.txt` contains all the unique words recognized in the corpus on
a single line, each separated by a space.

In the corpus code and in the markov model, each word is represented
by its' index in the vocabulary list. The first word in the line is
the 0th index.

### using the markov model

initialize a corpus object by giving it two arguments - the first is
the corpus file to use, and the second is the vocabulary file:

```python
c = corpus.read_data('corpus.txt', 'vocab.txt')
```

initialize a markov object with code that looks like this:

```python
m = Markov(corpus, 3)
```

where `corpus` is a corpus object, and `3` is the length of n-grams to use.

to generate text, call `Markov.generate(l)`, where `l` is the length
of the text you want to generate.


