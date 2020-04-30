class Road:
    _length = 0
    _width = 0

    def __init__(self, my_length, my_width):
        self._length = my_length
        self._width = my_width

    def mass_count(self, my_mass_for_unit, my_height):
        mass = self._length * self._width * my_mass_for_unit * my_height
        return mass


my_road = Road(20, 5000)
while True:
    try:
        mass_for_unit = float(input('Введите массу асфальта для покрытия одного кв. метра толщиной 1 см '))
        height = float(input('Введите толщину асфальта (в см) '))
        break
    except(ValueError, TypeError):
        print('Введите числа')
needed_mass = my_road.mass_count(mass_for_unit, height)
print('Необходимая масса полотна для покрытия {0:.0f}т'.format(needed_mass))
