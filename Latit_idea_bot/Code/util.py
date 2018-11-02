from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
import os
import io
import re
import spacy
# nlp = spacy.load('en')
# from spacy.tokenizer import Tokenizer
# tokenizer=Tokenizer(nlp.vocab)
import warnings
warnings.filterwarnings("ignore")
import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

porter_stem = PorterStemmer()
"Reading the data and converting sentences into tokens"

with open('MDE.txt') as f:
    text = f.read().lower()
text = sent_tokenize(text)

"removing stopwords"
filtered_sentence = []
filtered_sentence = [w for w in text if not w in stop_words]
for w in text:
    if w not in stop_words:
        filtered_sentence.append(w)

"converting sentence tokens into word tokens"

for sentence in text:
    text = nltk.pos_tag(filtered_sentence)
lemma_list_of_words = []

"Remove empty lists"
text = [x for x in text if x != []]
for i in range(0, len(text)):
    lemma1 = text[i]
    lemma2 = ''.join([lemmatizer.lemmatize(word) for word in lemma1])
    lemma_list_of_words.append(lemma2)

