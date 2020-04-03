import nltk
nltk.download('stopwords')
nltk.download('vader_lexicon')
import string
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

from nltk.tokenize import TweetTokenizer

stopwords = set(stopwords.words('english'))
analyzer = SentimentIntensityAnalyzer()

def remove_punctuation(tweet):
    return re.sub(r'[^\w\s]', '', tweet)

def remove_stopwords(tweet):
    return [w for w in tweet if w not in stopwords]

def analyze_sentiment(tweet):
    sentences = nltk.sent_tokenize(tweet)

    #filtered_sentences = [remove_punctuation(sentence) for sentence in sentences]
    #filtered_sentences = [remove_stopwords(sentence) for sentence in filtered_sentences]
    #scores = [analyzer.polarity_scores(sentence) for sentence in filtered_sentences]

    scores = [analyzer.polarity_scores(sentence) for sentence in sentences] # return example [{'neg': 0.0, 'neu': 0.686, 'pos': 0.314, 'compound': 0.4939}, {'neg': 0.0, 'neu': 0.758, 'pos': 0.242, 'compound': 0.4939}]
    sentiment_score = sum(score['compound'] for score in scores)/len(scores)
    return sentiment_score
