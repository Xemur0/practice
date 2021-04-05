class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        b1  = self.b + other.b
        if b1 < 0:
            return f'{self.a + other.a}{self.b + other.b}i'
        elif b1 == 0:
            return f'{self.a + other.a}'
        else:
            return f'{self.a + other.a}+{self.b + other.b}i'
    def __mul__(self, other):
        a1 = self.a * other.a
        a2 = self.b * other.b
        c = a1 - a2

        b1 = self.a * other.b
        b2 = self.b * other.a
        d = b1 + b2
        if d < 0:
            return f'{c}{d}i'
        elif c == 0:
            return f'{d}i'
        elif d == 0:
            return f'{c}'

        return f'{c}+{d}i'


    def __str__(self):
        if self.b < 0:
            return f'{self.a}{self.b}i'

        else:
            return f'{self.a}+{self.b}i'


a = ComplexNumber(1, 23)
b = ComplexNumber(1, 5)

print(a+b)
print(a*b)





