import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
import re
from nltk import word_tokenize,sent_tokenize


def get_article_content(url):

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    
    title = soup.find('meta', attrs={'name':"twitter:title"}).get('content')
    content = soup.find('div', attrs={'class':"pg-rail-tall__body"}).text

    return title, content

url = 'https://edition.cnn.com/2020/06/08/entertainment/ludacris-george-floyd-kid-nation/index.html'\

title, content = get_article_content(url)

def do_En_preprocessing(text):
    cleaned_content = re.sub(r'[^\w\d\s]','',text) # To remove symbols
    cleaned_content = cleaned_content.lower() # Case conversion, upper -> lower
    word_tokens = nltk.word_tokenize(cleaned_content) # Tokenization
    tokens_pos = nltk.pos_tag(word_tokens) # POS tagging
    NN_words = []   # To select nouns
    for word, pos in tokens_pos:
        if 'NN' in pos:
            NN_words.append(word)
            
    wlem = nltk.WordNetLemmatizer()   # Lemmatization
    lemmatized_words = []
    for word in NN_words:
        lemmatized_words.append(wlem.lemmatize(word))

    
    unique_NN_words = set(lemmatized_words)
    final_NN_words = lemmatized_words
    
    return final_NN_words

final_words = do_En_preprocessing(content)
from collections import Counter
c = Counter(final_words)

print(c.most_common(15))

from wordcloud import WordCloud
import matplotlib.pyplot as plt

total_words = ' '.join(final_words)

wordcloud = WordCloud(max_font_size=100, width=800, height=600, background_color='black')
wordcloud.generate(total_words)
plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
wordcloud.to_file("word_cloud_cnn.png")
