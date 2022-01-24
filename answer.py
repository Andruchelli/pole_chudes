class Answer: # ответ
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

        print("Вот задание на этот тур:")
        print(question) # вопрос
        return (
            question,
            answer,
            ["_"] * len(answer)
        )

    def ask_for_character(self): # определение буквы, введённой пользователем
        user_guess = input("Ваша буква: ")
        return user_guess[0]
        return(user_guess[0] if user_guess else ask_for_character())

    def open_characters_in(self, user_answer, answer, guess_character): # функция для проверки догадки и открытия соответствующих букв
        for index, correct_character in enumerate(answer):
            if correct_character == guess_character: # побуквенная проверка слова
                user_answer[index] = guess_character

        return user_answer
