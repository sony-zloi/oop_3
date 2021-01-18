'''
Задание 2
Создайте класс для конвертирования температуры из Цельсия в Фаренгейт и наоборот.
У класса должно быть два статических метода: для перевода из Цельсия в Фаренгейт и для перевода из Фаренгейта в Цельсий.
Также класс должен считать количество подсчетов температуры и возвращать это значение с помощью статического метода.
'''

from typing import List


class Converter:
    __count: int = 0
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

    @staticmethod
    def get_count() -> int:
        return Converter.__count


