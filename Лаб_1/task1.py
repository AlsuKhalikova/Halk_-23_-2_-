# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class HarryPotter:
    """
    Документация на класс.
    Класс описывает черты характера персонажа.
    """

    def __init__(self):
        """
        Инициализация экземпляра класса.

        Примеры:
        >>> harry_potter = HarryPotter()
        """
        self.attr1 = None
        self.attr2 = None

    def add_enough(self, arg1: str):
        """
        Метод добавляет enough к черте харакера.

        :param arg1: Черта характера

        Примеры:
        >>> harry_potter = HarryPotter()
        >>> harry_potter.add_enough('brave')
        """
        if not isinstance(arg1, str):
            raise TypeError("Черта характера должна быть типа str")
        self.attr1 = arg1 + ' enough'

    def add_too(self, arg2: str):
        """
        Метод добавляет too к черте харакера.

        :param arg2: Черта характера

        Примеры:
        >>> harry_potter = HarryPotter()
        >>> harry_potter.add_too('reckless')
        """
        if not isinstance(arg2, str):
            raise TypeError("Черта характера должна быть типа str")
        self.attr2 = 'too ' + arg2


class RonWeasley:
    """
    Документация на класс.
    Класс описывает черты характера персонажа.
    """

    def __init__(self):
        """
        Инициализация экземпляра класса.

        Примеры:
        >>> ron_weasley = RonWeasley()
        """
        self.attr1 = None
        self.attr2 = None

    def add_enough(self, arg1: str):
        """
        Метод добавляет enough к черте харакера.

        :param arg1: Черта характера

        Примеры:
        >>> ron_weasley = RonWeasley()
        >>> ron_weasley.add_enough('cheerful')
        """
        if not isinstance(arg1, str):
            raise TypeError("Черта характера должна быть типа str")
        self.attr1 = arg1 + ' enough'

    def add_a_little(self, arg2: str):
        """
        Метод добавляет a little к черте харакера.

        :param arg2: Черта характера

        Примеры:
        >>> ron_weasley = RonWeasley()
        >>> ron_weasley.add_a_little('vain')
        """
        if not isinstance(arg2, str):
            raise TypeError("Черта характера должна быть типа str")
        self.attr2 = arg2 + ' a little'


class HermioneGranger:
    """
    Документация на класс.
    Класс описывает черты характера персонажа.
    """

    def __init__(self):
        """
        Инициализация экземпляра класса.

        Примеры:
        >>> hermione_granger = HermioneGranger()
        """
        self.attr1 = None
        self.attr2 = None

    def add_very(self, arg1: str):
        """
        Метод добавляет very к черте харакера.

        :param arg1: Черта характера

        Примеры:
        >>> hermione_granger = HermioneGranger()
        >>> hermione_granger.add_very('smart')
        """
        if not isinstance(arg1, str):
            raise TypeError("Черта характера должна быть типа str")
        self.attr1 = 'very ' + arg1

    def add_too(self, arg2: str):
        """
        Метод добавляет too к черте харакера.

        :param arg2: Черта характера

        Примеры:
        >>> hermione_granger = HermioneGranger()
        >>> hermione_granger.add_too('pedantic')
        """
        if not isinstance(arg2, str):
            raise TypeError("Черта характера должна быть типа str")
        self.attr2 = 'too ' + arg2


if __name__ == "__main__":
    doctest.testmod()

    harry_potter = HarryPotter()
    harry_potter.add_enough('brave')
    harry_potter.add_too('reckless')
    print('Harry Potter is', harry_potter.attr1, 'and', harry_potter.attr2)

    ron_weasley = RonWeasley()
    ron_weasley.add_enough('cheerful')
    ron_weasley.add_a_little('vain')
    print('Ron Weasley is', ron_weasley.attr1, 'and', ron_weasley.attr2)

    hermione_granger = HermioneGranger()
    hermione_granger.add_very('smart')
    hermione_granger.add_too('pedantic')
    print('Hermione Granger is', hermione_granger.attr1, 'and', hermione_granger.attr2)
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
