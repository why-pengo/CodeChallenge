import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer


class ProcessText:
    # TODO: maybe add class var to count how many text are being handled

    def __init__(self, text):
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        self.__sentences = sent_tokenize(text)
        self.__words = word_tokenize(text)
        self.__tagged = None
        self.__phrases = None

    def get_sentences(self):
        return self.__sentences

    def get_words(self):
        return self.__words

    def process(self):
        grammar = "NP: {<DT><JJ>*<NN>}"
        cp = nltk.RegexpParser(grammar)
        self.__tagged = nltk.pos_tag_sents(word_tokenize(sent) for sent in self.__sentences)
        self.__phrases = cp.parse(self.__tagged[0])

    def get_tagged(self):
        return self.__tagged

    def get_phrases(self):
        return self.__phrases


