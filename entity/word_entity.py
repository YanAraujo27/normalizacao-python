class Word:
    def __init__(self, text: str):
        self.original_text = text
        self.normalized_text = []

    def set_normalized_text(self, text: str):
        self.normalized_text = text