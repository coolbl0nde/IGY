import re
from constants import amount_of_sentences_regexp
from constants import amount_of_non_dec_sentences
from constants import to_words_regexp
from constants import initials_regx
from constants import to_words_sentences_regexp
from constants import top_k_ngrams_regexp
from constants import abbreviations


def amount_of_sentences(text):
    reg = amount_of_sentences_regexp
    sentences = re.findall(reg, text)

    amount = len(sentences)

    for sentence in sentences:
        for abbreviation in abbreviations:
            if sentence.strip() == abbreviation:
                amount -= 1
        amount -= len(re.findall(initials_regx, sentence))

    return amount + amount_of_non_declarative_sentences(text)


def amount_of_non_declarative_sentences(text):
    reg = amount_of_non_dec_sentences
    sentences = re.findall(reg, text)

    amount = len(sentences)

    return amount


def to_words(text):
    reg = to_words_sentences_regexp
    sentences = re.findall(reg, text)

    words = []
    reg = to_words_regexp

    for sentence in sentences:
        words += re.findall(reg, sentence)

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


def get_top_k_ngrams(text, k, n):
    words = re.findall(top_k_ngrams_regexp, text.lower())
    ngrams = []
    answer = {}
    my_dict = {}

    for i in range(len(words) - n + 1):
        ngrams.append(''.join(words[i:i+n]))

    for value in ngrams:
        if value in my_dict:
            my_dict[value] += 1
        else:
            my_dict[value] = 1

    sorted_dict = dict(sorted(my_dict.items(), key = lambda x : x[1], reverse=True))

    i = 0

    for key, value in sorted_dict.items():
        if i < k:
            answer[key] = value
            i += 1
        else:
            break

    return answer

