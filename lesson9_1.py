from time import sleep

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        print(f"\033[31m{self.__color[0]}")
        sleep(7)
        print(f'\033[33m{self.__color[1]}')
        sleep(2)
        print(f'\033[32m{self.__color[2]}')
        sleep(7)
        print(f'\033[0mШо стоим кого ждем')

TrafficLight = TrafficLight()
TrafficLight.running()


