class Stationery:
    title = 'Title'
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('ручечкой рисую')

class Pencil(Stationery):
    def draw(self):
        print('карандашиком рисую')

class Handle(Stationery):
    def draw(self):
        print('маркером рисую')


d = Stationery()
a = Handle()
b = Pencil()
c = Pen()
d.draw()
a.draw()
b.draw()
c.draw()