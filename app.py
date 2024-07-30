from flask import Flask, render_template, request, jsonify
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import TFBertForSequenceClassification, BertTokenizer
import tensorflow as tf

app = Flask(__name__)

# Initialize VADER and BERT
vader_analyzer = SentimentIntensityAnalyzer()
model_name = 'nlptown/bert-base-multilingual-uncased-sentiment'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = TFBertForSequenceClassification.from_pretrained(model_name)

def classify_vader_sentiment(compound):
    if compound <= -0.6:
        return 'Very Negative'
    elif -0.6 < compound <= -0.2:
        return 'Negative'
    elif -0.2 < compound < 0:
        return 'Slightly Negative'
    elif compound == 0:
        return 'Neutral'
    elif 0 < compound <= 0.2:
        return 'Slightly Positive'
    elif 0.2 < compound <= 0.6:
        return 'Positive'
    else:
        return 'Very Positive'

def bert_sentiment_analysis(text):
    inputs = tokenizer(text, return_tensors='tf', truncation=True, padding=True, max_length=512)
    outputs = model(inputs)
    probs = tf.nn.softmax(outputs.logits, axis=-1)
    label = tf.argmax(probs, axis=-1).numpy()[0]
    return label, probs[0][label].numpy()

def classify_bert_sentiment(label):
    if label == 0:
        return 'Very Negative'
    elif label == 1:
        return 'Negative'
    elif label == 2:
        return 'Neutral'
    elif label == 3:
        return 'Positive'
    elif label == 4:
        return 'Very Positive'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    content = request.form['content']
    vader_sentiment = vader_analyzer.polarity_scores(content)['compound']
    vader_sentiment_class = classify_vader_sentiment(vader_sentiment)

    bert_label, bert_score = bert_sentiment_analysis(content)
    bert_sentiment_class = classify_bert_sentiment(bert_label)

    result = {
        'vader_sentiment': vader_sentiment_class,
        'bert_sentiment': bert_sentiment_class
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
