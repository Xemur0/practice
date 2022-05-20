class Division:
    def __init__(self, p_1, p_2):
        self.p_1 = p_1
        self.p_1 = p_2

    def div(self, p_1, p_2):
        try:
            return (p_1 / p_2)
        except:
            return (f'Деление на ноль')


a = Division(10, 0)
print(a.div(10, 4))
