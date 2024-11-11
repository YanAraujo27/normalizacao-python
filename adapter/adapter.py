from entity.word_entity import Word


class ConsoleInputOutput:
    def get_user_input(self) -> str:
        return input("Digite uma palavra desnormalizada: ")

    def display_result(self, word: Word):
        print(f"Palavra Original: {word.original_text}")
        print(f"Palavra Normalizada: {word.normalized_text}")