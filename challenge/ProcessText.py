import nltk
from nltk.tokenize import sent_tokenize, word_tokenize


class ProcessText:

    def __init__(self, text):
        nltk.download('punkt')
        self.__sentences = sent_tokenize(text)
        self.__words = word_tokenize(text)

    def get_sentences(self):
        return self.__sentences

    def get_words(self):
        return self.__words
