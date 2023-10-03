class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance

class Fabric:
    """Класс для демонстрации паттерна проектирования Фабрика"""
    def __init__(self):
        pass
    

class Facad:
    """Класс для демонстрации паттерна проектирования Фасад"""
    def __init__(self):
        pass

class Adapter:
    """Класс для демонстрации паттерна проктирования Адаптер"""
    pass


class Builder:
    """Класс для демонстрации паттерна проектирования Строитель"""

    

class Human:
    def __init__(self, name, surname, age, city):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city

  def __str__(self):
      return f'Объект с названием {self.name} {self.surname}'


# Добавить остальные паттерны проектирования которые я знаю, а именно:
# ФАБРИКА;
# СТРОИТЕЛЬ;
# ФАСАД;
# АДАПТЕР;
