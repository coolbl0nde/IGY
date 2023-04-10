amount_of_sentences_regexp = r"[^.!?]*\.{1,3}"
amount_of_non_dec_sentences = r"[?!]+"
initials_regx = r"(\b[A-Z]\.)"
to_words_sentences_regexp = r"\s*([^.!?]+)*[.!?]"
to_words_regexp = r'\b\w*[a-zA-Z]\w*\b'
top_k_ngrams_regexp = r'\b\w+\b'
abbreviations = ["Mr.", "Mrs.", "Dr.", "etc."]