class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.ispolice = is_police

    def go(self):
        return f'{self.name} {self.color} Погнала'
    def stop(self):
        return f'{self.name} {self.color} Остановилась'
    def turn(self, direction):
        return f'{self.name} {self.color} Повернула {direction}'
    def show_speed(self):
        return f'Скорость {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police = True):
        super().__init__(speed, color, name, is_police = False)

    def show_speed(self):
        if self.speed > 60:
            return f'Нарушил скоростной режим {self.speed}'
        else:
            return f'Скорость {self.speed}'

class  SportCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police=False)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        if self.speed > 40:
            return f'Нарушил скоростной режим - текущая скорость {self.speed}'
        else:
            return f'Скорость {self.speed}'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police=True)


a = WorkCar(29, 'черная', 'Mazda')
b = PoliceCar(120, 'белая', 'Lada' )
print(a.show_speed())
print(b.turn('Налево'))
print(a.go(), a.turn('Домой'), a.stop(), a.show_speed(), sep=',')
c = SportCar(120, 'зеленая', 'Honda')
print(c.go(), c.turn('на автодром'), c.stop(), c.show_speed(), sep=',')



