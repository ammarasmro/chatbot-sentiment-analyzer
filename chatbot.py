from model.model_client import SentimentAnalyzer

print("Hi, let's start talking!")

analyzer = SentimentAnalyzer()

day = 0
sentences = []
sentiments = []

def show_daily_sentiment():
    print('Daily sentiment for day #{} is: {}'.format(day, average_sentiment))

def show_stats():
    print('Statistics of sentiment over time')
    print('Days: {}'.format(day))
    print('Number of days of happiness: {}'.format(days_happy))


while True:
    sentence = input()
    if sentence == 'how is my day going?': show_daily_sentiment()
    elif sentence == 'show stats': show_stats()
    elif sentence == 'day':
        day += 1
        how_day_was = input('How was your day?')
        labels_for_today = 'POSITIVE' if how_day_was == 'good' else 'NEGATIVE'
        # model.fit(daily_conversation, labels_for_today)
    elif sentence == 'stop': break
    else:
        print(analyzer.sentence_to_sentiment(sentence))
    # model.fit(sentence)
