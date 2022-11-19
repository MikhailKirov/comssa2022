import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

def evaluate_sentiment(input_string):
    try:
        sentiment_list = ['Strongly Negative', 'Negative', 'Neutral', 'Positive', 'Strongly Positive']
        analyser = SentimentIntensityAnalyzer()
        result = analyser.polarity_scores(input_string)
        value = abs(result['compound'])
        try:
            sign = (result['compound'])/(abs(result['compound']))
        except:
            sign = 1
        output = int(round((pow(value,0.5) * sign)+2,0))
    except:
        output = 'Unable to Ascertain Sentiment'
    return sentiment_list[output]

#print(evaluate_sentiment("Hello fellow humans that i am going to kill"))