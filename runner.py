from engine import Engine

e = Engine('questions.yml')
result = e.start_game()

print("Пользователь победил?", result)
