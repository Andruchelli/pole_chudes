import yaml 

class Loader:
    def __init__(self, filename):
        # Здесь может приниматься имя файла, откуда грузим вопросы...
        # Можно также принимать аргумент "сложность". В этом случае в зависимости от сложности
        # вопросы грузятся из файла teen.yml, adult.yml и т.д.
        # pass
        self.filename = filename

    def load(self):
        # сделать загрузку из файла
        file = open(self.filename, 'r', encoding="utf8")
        return yaml.safe_load(file.read())

        # return (
            # (
            #    "Тёмный ангел автотюна.",
            #    "bladee"
            # ),
            # (
            #    "Рэппер и дизайнер из объединения Drain Gang.",
            #    "ecco2k"
            # ),
            # (
            #    "Депортированный из Швеции фрэшмен с тайскими корнями.",
            #    "thaiboy"
            # )
        # )
