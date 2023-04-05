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

