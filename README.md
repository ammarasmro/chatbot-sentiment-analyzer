# Chatbot Sentiment Analyzer

This is my attempt to build an interactive sentiment analyzer. It is designed to work with a chatbot.

The goal was to build a model that can accept sentences from a human and judge whether the human is having a good day or not. This will come in handy for my chatbot to make the experience more personal.

## Data
The data used here is just tweets with the sentiment. Training and testing data were obtained from a [Kaggle Competition]

## The model
The model uses an embedding layer, Long Short Term Memory units in the hidden layer, and a dense layer to predict sentiment in a sequential manner. I believe that this architecture fits this kind of data more than a classifier.
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
embedding_2 (Embedding)      (None, 200, 128)          4479232   
_________________________________________________________________
lstm_2 (LSTM)                (None, 100)               91600     
_________________________________________________________________
dense_2 (Dense)              (None, 1)                 101       
=================================================================
Total params: 4,570,933
Trainable params: 4,570,933
Non-trainable params: 0
_________________________________________________________________
None
```

## Results
After 3 epochs, the accuracy was ok

stage | accuracy (%)
--- | :---:
training | 88.8
validation | 70.3
testing | 76.1

Although this seemed daunting at first but interacting with the model showed promising results. For now I'm assuming that the noise in the tweets is what causing the decrease in accuracy for example people tweet emojis and deform words by repeating or changing characters.

Some examples of my interaction with the model

> 0 is sad | 1 is happy

input sentence | sentiment
--- | :---:
today was a very bad day I got left out i hate my life loser bad behaviour from colleague | 0.009026654
today was the best day ever i loved it i enjoyed it | 0.9838071
my girlfriend dumped me | 0.051465746
She does love me | 0.6479154
She doesnt love me | 0.18961194
I got a job | 0.70725995
I lost my job | 0.11154106
I got the job done | 0.9407746

## Usage
Just run the chatbot file and enter sentences for now. It's get better I promise.

```bash
git clone https://github.com/ammarasmro/chatbot-sentiment-analyzer.git
cd chatbot-sentiment-analyzer
python3 chatbot.py
```

> PS: Sorry of the extra data. I need it for easy access when I train models

[Kaggle Competition]: https://www.kaggle.com/c/twitter-sentiment-analysis2 "Kaggle"
