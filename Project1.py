import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from textblob import TextBlob
import spacy

def tokens_maker(text):
    tokens = word_tokenize(text)
    tokens = [word.lower() for word in tokens]
    tokens = [word for word in tokens if word not in string.punctuation]
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words]
    
    return tokens

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
        
    if polarity >= 0.1:
        x = 'positiv'
    elif polarity <= -0.1 :
        x = "Negative"
    else:
        x = "Neutral"
    
    print("Score" , polarity)
    print("Label is :" , x)
    return {
        'polarity': polarity ,
        'text' : text ,
        "label" : x
    }

def extract_entities(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    dic = {}
    for ent in doc.ents:
        if ent.label_ not in dic:
            dic[ent.label_] = []
        dic[ent.label_].append(ent.text)
    return dic
def find_top_words(tokens , top=5 ):
    word_freq = {}
    for word in tokens:
        word_freq[word]= word_freq.get(word , 0) + 1

    top_words = sorted(word_freq.items() , key = lambda x: x[1], reverse = True)[:top]
    return top_words


Text = """Apple Inc. was founded by Steve Jobs and is one of the most valuable companies in the world. 
The company makes amazing products. I love Apple products! Tim Cook is the CEO. Google and Microsoft 
are also great tech companies. The technology industry is growing fast."""


print('It is the text :' , Text)
cleaned_text = ' '.join(tokens_maker(Text))
print("The number of tokens of the text after filter:" , len(cleaned_text.split()))
print(cleaned_text)
print("****************************")
analyze_sentiment(cleaned_text)
print("The key words are:" , extract_entities(cleaned_text))
top_words = find_top_words(tokens_maker(Text), top=5)
print("Top keywords:", top_words)
