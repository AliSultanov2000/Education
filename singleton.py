class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance

plt.figure(figsize=(7, 5))

x = range(20)  
y = [i ** 2 for i in x]

plt.plot(x, y,
        label='quadratic function',  
        marker='o', markersize=4)

plt.title('Example of graph')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.show()
