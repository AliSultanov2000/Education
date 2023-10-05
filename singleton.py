class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance

class Fabric:
    """Класс для демонстрации паттерна проектирования Фабрика"""
    def __init__(self, f1, f2):
        self.f1 = f1
        self.f2 = f2 
    



class Adapter(Human):
    """Класс для демонстрации паттерна проктирования Адаптер"""
    def __init__(self, name, surname):
        print(name)
        print(surname)


class Builder:
    """Класс для демонстрации паттерна проектирования Строитель"""
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    

class Human:
    def __init__(self, name, surname, age, city):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city

  def __str__(self):
      return f'Объект с названием {self.name} {self.surname}'

 def __len__(self):
     return len([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])





