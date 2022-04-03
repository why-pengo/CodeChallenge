import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from collections import Counter
from itertools import chain
import string


class ProcessText:
    # TODO: maybe add class var to count how many texts are being handled

    def __init__(self, text):
        nltk.download('punkt', quiet=True)
        nltk.download('averaged_perceptron_tagger', quiet=True)
        self.__sentences = sent_tokenize(text)
        import re
        no_punct = re.sub("’", '', text)       # Strange encoding
        no_punct = re.sub("”", '', no_punct)   # Strange encoding
        no_punct = re.sub("“", '', no_punct)   # Strange encoding
        translator = str.maketrans('', '', string.punctuation)
        no_punct = no_punct.translate(translator)
        self.__words = word_tokenize(no_punct)
        self.__tagged = None
        self.__phrases = None
        self.__top100 = None

    def get_sentences(self):
        return self.__sentences

    def get_words(self):
        return self.__words

    def process(self):
        self.__phrases = list(nltk.trigrams(self.__words))
        self.__top100 = Counter(chain(self.__phrases)).most_common(100)

    def get_tagged(self):
        return self.__tagged

    def get_phrases(self):
        return self.__phrases

    def get_top_100(self):
        rv = str()
        for i in self.__top100:
            rv += f"{' '.join(i[0])} = {i[1]}\n"
        return rv

