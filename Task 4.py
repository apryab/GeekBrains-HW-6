class Car:
    speed = 0
    color = ''
    name = ''
    is_police = bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print('Текущая скорость равна:', self.speed)

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Машина повернула', direction)


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        print('Текущая скорость равна:', self.speed)

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Машина повернула', direction)


class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        try:
            if float(self.speed) > 60:
                print('Нарушение скорости')
        except(ValueError, TypeError):
            print('Ошибка в данных')
        print('Текущая скорость равна:', self.speed)

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Машина повернула', direction)


class WorkCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        try:
            if self.speed > 40:
                print('Нарушение скорости')
        except(ValueError, TypeError):
            print('Ошибка в данных')
        print('Текущая скорость равна:', self.speed)

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Машина повернула', direction)


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

    def show_speed(self):
        print('Текущая скорость равна:', self.speed)

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Машина повернула', direction)


my_work_car = WorkCar(30, 'yellow', 'best_car')
my_town_car = TownCar(70, 'blue', 'best_car')
my_police_car = PoliceCar(30, 'grey', 'best_car')
my_sport_car = SportCar(120, 'red', 'my_car')
my_town_car.go()
print(my_police_car.is_police)
my_town_car.show_speed()
