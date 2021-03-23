class Worker:
    def __init__(self, name, surname, position, income, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income
        self.bonus = {'wage': income, 'bonus': bonus}
class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self.bonus.get('wage') + self.bonus.get('bonus')


a = Position('Aleks', 'Prfnk', 'Sound engineer', 500, 100)

print(a.get_full_name())
print(a.get_total_income())
print(a.position)


