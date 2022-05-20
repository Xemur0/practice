class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_road(self):
        mass = 25
        thik = 0.05
        return self._length * self._width * mass * thik

a = Road(5000, 20)
print(a.calc_road())
