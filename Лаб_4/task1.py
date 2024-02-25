import doctest


class Cat:
    """
    Класс, который описывает котёнка.
    """
    def __init__(self, name: str, age: int):
        """
        Создание и подготовка к работе объекта "Котёнка"
        :param name: Кличка котёнка
        :param age: Возраст котёнка
        Примеры:
        >>> cat = Cat("Barsik", 1)
        """
        self._name = name  # Наследуем атрибуты name и age
        self.age = age  # Инициализируем публичный атрибут, отработает setter свойства

    @property
    def name(self) -> str:
        """Возвращает кличку котёнка."""
        return self._name

    @property
    def age(self) -> int:
        """Возвращает возраст котёнка."""
        return self._age

    @age.setter
    def age(self, new_age: int) -> None:
        """Устанавливает новый возраст котёнка."""
        if not isinstance(new_age, int):
            raise TypeError("Возраст котёнка должен быть числом типа int")
        if new_age <= 0:
            raise ValueError("Возраст котёнка должен быть положительным числом")
        self._age = new_age

    def __str__(self) -> str:
        """Метод, предназначенный для чтения."""
        return f"Кличка котёнка {self.name}. Возраст {self.age}."

    def __repr__(self) -> str:
        """Возвращает строку, показывающую, как может быть инициализирован экземпляр."""
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age})"

    def cuteness(self) -> str:
        """Реализация метода, который возвращает строку степени миловидности котёнка."""
        return "Милый"


class SiberianCat(Cat):
    """Класс, который описывает сибирского котёнка, как одного из видов котят."""
    def __init__(self, name: str, age: int, coloration: str):
        """
        Создание и подготовка к работе объекта "Сибирский котёнок",
        дочерний класс объекта "Котёнок"
        :param name: Кличка котёнка
        :param age: Возраст котёнка
        :param coloration: Цвет окраса котёнка
        Примеры:
        >>> cat_1 = SiberianCat("Васька", 3, "Серый")
        """
        super().__init__(name, age)  # Инициализируем защищенный атрибут, чтобы его нельзя было изменить
        self._coloration = coloration  # Инициализируем защищенный атрибут, чтобы его нельзя было изменить

    @property
    def coloration(self) -> int:
        """Возвращает цвет окраса котёнка."""
        return self._coloration

    def __str__(self) -> str:
        """Метод, предназначенный для чтения."""
        return f"Кличка котёнка {self._name}. Возраст {self._age}. Цвет окраса котёнка {self.coloration} "

    def __repr__(self) -> str:
        """Возвращает строку, показывающую, как может быть инициализирован экземпляр."""
        return f"{self.__class__.__name__}(name={self._name!r}, age={self._age}, coloration={self.coloration}) "

    def cuteness(self) -> str:
        """Перегрузка метода, чтобы он возвращал степень миловидности конкретной породы."""
        return "Очень милый"


if __name__ == "__main__":
    doctest.testmod()
    pass
