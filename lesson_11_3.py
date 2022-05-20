import sys

class NumericList:
    def __init__(self, *p):
        self.p = p
    some_list = []
    def input(self):
        while True:
            try:
                self.p = int(input('Введите число:'))
                self.some_list.append(self.p)

            except:
                print(f'Вы ввели не цифру')
                print(f'Продолжить? y/n: ', end='')
                answer = input()
                if answer == 'n':
                    print(f'Список - {self.some_list}')
                    sys.exit(0)
                elif answer == 'y':
                    continue

a = NumericList(1)
print(a.input())