class Loader:
    def __init__(self, filename):
        # Здесь может приниматься имя файла, откуда грузим вопросы...
        # Можно также принимать аргумент "сложность". В этом случае в зависимости от сложности
        # вопросы грузятся из файла teen.yml, adult.yml и т.д.
        # pass
        self.tasks = self.load()

    def load(self, filename):
        # сделать загрузку из файла
        file = open(filename, 'r', encoding="utf8")
        raw_data = yaml.safe_load(file.read())
        tasks = {}

        return tasks

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
