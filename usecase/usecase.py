from entity.word_entity import Word


class Normalizer:
    def normalize(self, word: Word):
        if word.original_text.lower().strip() == "logica":
            normalized_text = "logical"
        else:
            normalized_text = word.original_text.strip().lower()

        word.set_normalized_text(normalized_text)