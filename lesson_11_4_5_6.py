class Orgtechnic:
    def __init__(self, name, price, count, number_of_lists):
        self.name = name
        self.price = price
        self.count = count
        self.numb = number_of_lists
        self.wh_full = []
        self.wh = []
        self.technic = {'Model': self.name, 'Price': self.price, 'Count': self.count}

    def __str__(self):
        return f'{self.name} have price {self.price} count {self.count}'

    def reception(self):

        try:
            unit = input(f'Input name: ')
            unit_p = int(input(f'Price 1 unit: '))
            unit_q = int(input(f'Inout count: '))
            unique = {'Model': unit, 'Price': unit_p, 'Count': unit_q}
            self.technic.update(unique)
            self.wh.append(self.technic)
            print(f'Current List -\n {self.wh}')
        except:
            return f'Error input'

        print(f'to Quit - Q, to continue - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.wh_full.append(self.wh)
            print(f'all WH -\n {self.wh_full}')
            return f'Exit'
        else:
            return Orgtechnic.reception(self)


class Printer(Orgtechnic):
    def to_print(self):
        return f'Something print {self.numb} times'


class Scanner(Orgtechnic):
    def to_scan(self):
        return f'Something scan {self.numb} times'


class Copier(Orgtechnic):
    def to_copy(self):
        return f'Something copy {self.numb} times'


technic_1 = Printer('hp', 1000, 2, 10)
technic_2 = Scanner('canon', 1357, 5, 1)
technic_3 = Copier('xerox', 3443, 1, 5)
print(technic_1.reception())
print(technic_1.to_print())
print(technic_3.to_copy())
print(technic_2.to_scan())

