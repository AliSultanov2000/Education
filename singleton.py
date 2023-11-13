class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance


vals = [24, 17, 53, 21, 35]
labels = ["Ford", "Toyota", "BMW", "Audi", "Jaguar"]
explode = (0, 0, 0.1, 0, 0)

plt.pie(vals, labels=labels,
        explode=explode,
        autopct='%1.1f%%',
        shadow=True)

plt.title("Распределение марок автомобилей на дороге")
plt.show()
