#!/usr/bin env python
# mapping from votesmart IDs to congressperson names
import yaml
import os

# open the author info from yaml data.
# this is only data for congresspeople with votesmart IDs.
stream = open('static/author-mapping/votesmart.yml', 'rb')
data = yaml.load(stream)

# create dictionary of Name -> VoteSmart ID
mapping = [(' '.join([author['name']['first'],
                      author['name']['last']]),
            author['id']['votesmart'],) for author in data]

mapping = [(k,v) for (k,v) in mapping if str(v) in os.listdir('corpora')]

mapping = dict(mapping)
