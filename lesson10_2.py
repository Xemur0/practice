from abc import ABC, abstractmethod

class Material(ABC):
    result = 0
    def __str__(self):
        return f'{Material.result}'
    @property
    @abstractmethod
    def summary_material(self):
        pass


class Coat(Material): #Пальто
    def __init__(self, v):
        self.value = v
        self.square_coat = round(v/6.5 + 0.5)
        Material.result += self.square_coat
    @property
    def summary_material(self):
        return self.square_coat
    def __str__(self):
        return f'Расход требуемой ткани на пальто  {self.square_coat}'

class Jacket(Material): #Костюм
    def __init__(self, h):
        self.height = h
        self.square_jacket = round((2*h + 0.3)/100)
        Material.result += self.square_jacket
    @property
    def summary_material(self):
        return self.square_jacket
    def __str__(self):
        return f'Расход требуемой ткани на костюм {self.square_jacket}'



coat = Coat(42)
jacket = Jacket(250)
print(coat)
print(jacket)
print(Material)


