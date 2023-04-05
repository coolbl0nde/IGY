import re

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