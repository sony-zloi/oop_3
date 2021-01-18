"""Задание 3
Создайте класс для перевода из метрической системы в английскую и наоборот.
Функциональность необходимо реализовать в виде статических методов.
Обязательно реализуйте перевод мер длины."""


class Converter:
    km: float
    mile: float

    @staticmethod
    def metr_to_eng() -> dict:
        return {"miles": Converter.km / 1.609, "yards": Converter.km * 1094, "foots": Converter.km * 3281}

    @staticmethod
    def eng_to_metr() -> dict:
        return {"Километры": Converter.mile * 1.609, "Метры": Converter.mile * 1609, "Сантиметры": Converter.mile \
                                                                                                   * 160934}

