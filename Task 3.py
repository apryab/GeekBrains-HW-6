class Worker:
    name = ''
    surname = ''
    position = ''
    _income = dict()

    def __init__(self, my_name, my_surname, my_position,
                 my_wage, my_bonus):
        self.name = my_name
        self.surname = my_surname
        self.position = my_position
        self._income = {'wage': my_wage, 'bonus': my_bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name

    def get_total_income(self):
        temp_list = self._income.values()
        final_payment = 0
        try:
            for elem in temp_list:
                final_payment += float(elem)
            return final_payment
        except(TypeError, ValueError):
            return 'Ошибка в данных'


my_position_test = Position('Anton', 'Ivan', 'Analytic', 56, 35)
print('Имя работника -', my_position_test.get_full_name())
print('Полная зарплата сотрудника -', my_position_test.get_total_income())
