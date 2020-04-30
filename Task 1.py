import time


class TrafficLight:
    __color = 'красный'

    def running(self):
        if self.__color == 'красный':
            print('Текущий цвет -', self.__color)
            time.sleep(7)
            if self.__color == 'красный':
                self.__color = 'жёлтый'
                print('Текущий цвет -', self.__color)
                time.sleep(2)
                if self.__color == 'жёлтый':
                    self.__color = 'зелёный'
                    print('Текущий цвет -', self.__color)
                    time.sleep(5)
                    self.__color = 'красный'
                    print('Цикл светофора закончен')
                    return
        print('Нарушение порядка')
        return


traffic_light = TrafficLight()
traffic_light.running()
