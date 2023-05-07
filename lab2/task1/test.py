import unittest
import utilites

class TestSentenceAmountMethod(unittest.TestCase):

    def test_general_amount_0(self):
        result = utilites.amount_of_sentences("")
        self.assertEqual(result, 0)

    def test_general_amount_2(self):
        result = utilites.amount_of_sentences("Abc. Ahd...")
        self.assertEqual(result, 2)

    def test_general_amount_3(self):
        result = utilites.amount_of_sentences("Abc. Ahd... Hjdjjd. Hjdjddhkf!")
        self.assertEqual(result, 4)

    def test_non_declarative_amount_1(self):
        result = utilites.amount_of_non_declarative_sentences("Abc. Ahd... Hjdjjd. Hjdjddhkf!")
        self.assertEqual(result, 1)

    def test_non_declarative_amount_3(self):
        result = utilites.amount_of_non_declarative_sentences("Abc?? Ahd?! Hjdjjd. Hjdjddhkf!")
        self.assertEqual(result, 3)

    def test_non_declarative_amount_0(self):
        result = utilites.amount_of_non_declarative_sentences("Abc... Ahd. Hjdjjd.")
        self.assertEqual(result, 0)

    def test_sentences_length_4(self):
        result = utilites.sentences_length("Abc... Ahd. Hjdjjd.")
        self.assertEqual(result, 4)

    def test_sentences_length_5(self):
        result = utilites.sentences_length("Abc?? Ahd?! Hjdjjd. Hjdjddhkf!")
        self.assertEqual(result, 3)

    def test_words_length_4(self):
        result = utilites.words_length("Abc... Ahd. Hjdjjd.")
        self.assertEqual(result, 4)

    def test_words_length_5(self):
        result = utilites.words_length("Abc?? Ahd?! Hjdjjd. Hjdjddhkf!")
        self.assertEqual(result, 5.25)

    def test_top_k_ngrams_4(self):
        result = utilites.get_top_k_ngrams("Abc... Ahd. Hjdjjd.", 3, 1)
        self.assertEqual(result, {'abc': 1, 'ahd': 1, 'hjdjjd': 1})

    def test_top_k_ngrams_5(self):
        result = utilites.get_top_k_ngrams("Abc... Ahd. Hjdjjd. Abc.", 3, 1)
        self.assertEqual(result, {'abc': 2, 'ahd': 1, 'hjdjjd': 1})