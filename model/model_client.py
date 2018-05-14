import os

import numpy as np

from keras.models import load_model

class SentimentAnalyzer:
    def __init__(self):
        self.model = load_model(os.path.join('model','rnn_model.h5'))
        self.get_dictionaries_ready()

    def get_dictionaries_ready(self):
        self.word2id = {}
        self.id2word = {}
        with open(os.path.join('data','word2id.txt'),'r') as f:
            text = f.readlines()
        for line in text:
            word, _id = line.split()
            self.word2id[word] = int(_id)
            self.id2word[_id] = word

    def sentence_to_sentiment(self, text):
        text = text.lower().split()
        sentence_of_ids = [self.word2id[word] for word in text if word in self.word2id]
        padding = [0 for _ in range(200 - len(sentence_of_ids))]
        padded_sequence = padding + sentence_of_ids
        return self.model.predict(np.array([padded_sequence]))[0][0]
