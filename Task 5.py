class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def __init__(self):
        super().__init__('Pen')

    def draw(self):
        print('Запуск отрисовки кота')


class Handle(Stationery):

    def __init__(self):
        super().__init__('Handle')

    def draw(self):
        print('Запуск отрисовки слона')


class Pencil(Stationery):

    def __init__(self):
        super().__init__('Pencil')

    def draw(self):
        print('Запуск отрисовки собаки')


my_stationery_1 = Pen()
my_stationery_2 = Pencil()
my_stationery_3 = Handle()
my_stationery_1.draw()
my_stationery_2.draw()
my_stationery_3.draw()
