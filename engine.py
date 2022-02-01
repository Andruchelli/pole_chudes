import random
from loader import Loader
from task import Task

class Engine:
    def __init__(self, filename, tries = 10):
        loader = Loader(filename)
        # Подготавливаем все задания (впрочем, можно сначала выбирать 1 задание, а потом подготавливать только его)
        all_tasks = self.__prepare_tasks(loader.load())

        self.task = random.choice(all_tasks)
        self.tries = tries


    def start_game(self):
        print("Добро пожаловать на Поле Чудес! Главный приз сегодня - АААААВТОМОБИЛЬ!!!")
        print("Вот задание на этот тур:")
        print(self.task.question)

        success = self.next_turn()

        if success:
            print("Действительно, это слово", self.task.answer)
            print("И перед нами победитель!!!")
        else:
            print("Вы использовали все попытки. Компьютер победил")

        return success


    def next_turn(self):
        if self.tries <= 0: return False

        print("Ваше слово:", self.task.guess_word)

        guess_character = self.__ask_for_character()
        result = self.task.open_characters(guess_character)

        if result:
            print("Откройте, пожалуйста, букву", guess_character)
        else:
            print("Нет буквы " + guess_character + " в этом слове!")
            self.tries -= 1
            print("У вас осталось " + str(self.tries) + " попыток")

        return(
            True if self.task.answer == self.task.guess_word else self.next_turn()
        )


    def __prepare_tasks(self, raw_tasks):
        # Делаем список из образцов класса Task...
        tasks = {}
        for raw_task in raw_tasks:
            task = Task(raw_task['question'], raw_task['answers'])
        return list(map(lambda raw_task: Task(raw_task), raw_tasks))


    # функция для определения буквы, введённой пользователем
    def __ask_for_character(self):
        user_guess = input("Ваша буква: ")
        return(user_guess[0] if user_guess else self.__ask_for_character())
