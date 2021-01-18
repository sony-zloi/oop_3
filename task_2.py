'''
Задание 2
Создайте класс для конвертирования температуры из Цельсия в Фаренгейт и наоборот.
У класса должно быть два статических метода: для перевода из Цельсия в Фаренгейт и для перевода из Фаренгейта в Цельсий.
Также класс должен считать количество подсчетов температуры и возвращать это значение с помощью статического метода.
'''

from typing import List


class Converter:
    __report: List[float] = []
    __count: int = 0
<<<<<<< HEAD
    far: float
    celsius: float

    def __init__(self):
        Converter.__count += 1

    @staticmethod
    def cel_to_far() -> float:
        return Converter.celsius * 9 / 5 + 32

    @staticmethod
    def far_to_cel() -> float:
        return (Converter.far - 32) * 5 / 9
=======

    def __init__(self, celsius: float):
        self.celsius = celsius
        Converter.__count += 1
        self.__report.append(celsius)

    # def set_cel(self, value):
    #     self.celsius = value
    #
    # def set_far(self, value):
    #     self.far = value

    def cel_to_far(self) -> float:
        return self.celsius * 9/5 + 32

    @classmethod
    def get_report(cls) -> List[float]:
        return cls.__report

    @staticmethod
    def get_count() -> int:
        return Converter.__count

temp1 = Converter(30.0)
temp2 = Converter(32.0)
temp3 = Converter(30.0)
assert temp1.cel_to_far() == 86.0
print(temp1.get_report())
print(Converter.get_count())

>>>>>>> 6dcc88026b4e08a1d858a772b3aaeec51e7e8151

    @staticmethod
    def get_count() -> int:
        return Converter.__count

