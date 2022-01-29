class Task:
    def __init__(self, raw_task):
        self.question = raw_task[0]
        self.answer = list(raw_task[1])
        self.guess_word = ["_"] * len(self.answer)


    # функция для проверки догадки и открытия соответствующих букв
    def open_characters(self, guess_character):
        found_any = False # нашлось ли соответствие?

        for index, correct_character in enumerate(self.answer):
            if correct_character == guess_character: # побуквенная проверка слова
                self.guess_word[index] = guess_character
                found_any = True

        return found_any