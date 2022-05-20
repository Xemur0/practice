class Cell:
    def __init__(self, qnt):
        self.qnt = int(qnt)

    def __str__(self):
        return f'result {self.qnt * "*"}'

    def __add__(self, other):
        return Cell(self.qnt + other.qnt)

    def __sub__(self, other):
        return self.qnt - other.qnt if (self.qnt - other.qnt) > 0 else print('negative')



    def __mul__(self, other):
        return Cell(int(self.qnt * other.qnt))

    def __truediv__(self, other):
        return Cell(round(self.qnt // other.qnt))


    def make(self, rows):
        row = ''
        for i in range(int(self.qnt / rows)):
            row += f'{"*" * rows} \\n'
        row += f'{"*" * (self.qnt % rows)}'
        return row

cells1 = Cell(10)
cells2 = Cell(3)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make(6))
print(cells1.make(11))
print(cells1 / cells2)