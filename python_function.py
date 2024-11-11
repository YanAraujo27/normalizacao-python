from adapter.adapter import ConsoleInputOutput
from entity.word_entity import Word
from usecase.usecase import Normalizer


class ApplicationController:
    def __init__(self, normalizer: Normalizer, io: ConsoleInputOutput):
        self.normalizer = normalizer
        self.io = io

    def run(self):
        user_input = self.io.get_user_input()
        word = Word(user_input)
        self.normalizer.normalize(word)
        self.io.display_result(word)

# Inicializa e executa a aplicação
if __name__ == "__main__":
    normalizer = Normalizer()
    io = ConsoleInputOutput()
    app = ApplicationController(normalizer, io)
    app.run()