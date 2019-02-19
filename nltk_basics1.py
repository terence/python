#!/usr/local/bin/python3
# Tutorial https://www.nltk.org/book/ch01.html


print ("Scipy Processing")

import sys
print (sys.path)

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.book import *
import matplotlib

# nltk.download()


data = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

print(word_tokenize(data))
	  
phrases = sent_tokenize(data)
words = word_tokenize(data)

print(phrases)
print(words)

wordsFiltered = []

# Stopwords
# ==============
stopWords = set(stopwords.words('english')) 
for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)
 
print(wordsFiltered)
print(len(stopWords))
print(stopWords)


text1.similar("monstrous")
text2.similar("monstrous")

text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])









