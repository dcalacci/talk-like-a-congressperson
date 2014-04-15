from flask import Flask, render_template, request, redirect, url_for
import corpus
import markov
from author_mapping import mapping

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html',
                           congresspeople=sorted(mapping.keys()))


@app.route('/generate', methods=['GET'])
def generate():
    name = request.args.get('congressperson')
    print "'", name, "'"
    ngram_length = int(request.args.get('ngram_length'))
    text_length = int(request.args.get('text_length'))
    return redirect(url_for('generate_text',
                            author_id=mapping[name],
                            ngram=ngram_length,
                            length=text_length))


@app.route('/congressperson/<int:author_id>')
def uh_text(author_id):
    return str(author_id)


@app.route('/congressperson/<int:author_id>/generate/<int:ngram>/<int:length>')
def generate_text(author_id, ngram, length):
    c = corpus.read_data('corpora/' + str(author_id) + '/corpus.txt',
                         'vocab.txt')
    m = markov.Markov(c, ngram)

    return m.generate(length)

if __name__ == '__main__':
    app.run(debug=True)
