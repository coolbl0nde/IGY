import re
from collections import Counter

abbreviations = ["Mr.", "Mrs.", "Dr.", "etc."]


def amount_of_sentences(text):
    reg = r"[^.!?]*\.{1,3}"
    sentences = re.findall(reg, text)

    amount = len(sentences)

    for sentence in sentences:
        for abbreviation in abbreviations:
            if sentence.strip() == abbreviation:
                amount -= 1

    print(amount)
    return amount


def amount_of_non_declarative_sentences(text):
    reg = r"[?!]+"
    sentences = re.findall(reg, text)

    amount = len(sentences)

    print(amount)
    return amount


def to_words(text):
    reg = r'\s*([^.!?]+)*[.!?]'
    sentences = re.findall(reg, text)

    words = []
    reg = r'\b\w*[a-zA-Z]\w*\b'

    for sentence in sentences:
        words += re.findall(reg, sentence)

    print(words)
    return words


def characters_in_text(text):
    words = to_words(text)
    amount = 0

    for word in words:
        amount += len(word)

    return amount


def sentences_length(text):
    amount = amount_of_sentences(text) + amount_of_non_declarative_sentences(text)
    characters = characters_in_text(text)

    return characters/amount


def words_length(text):
    amount = len(to_words(text))
    characters = characters_in_text(text)

    return characters/amount


def get_top_k_ngrams(text, k = 10, n = 4):
    finished_text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())

    words = finished_text.split()
    ngrams = [tuple(words[i:i + n]) for i in range(len(words) - n + 1)]
    ngram_counts = Counter(ngrams)

    return ngram_counts.most_common(k)

