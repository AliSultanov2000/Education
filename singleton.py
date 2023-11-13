class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance


plt.bar([1, 2, 3], [10, 20, 30],
        width=0.45,
        alpha=0.6,  # Прозрачность,
        color = ['red', 'green', 'blue']
        )

plt.title('Simple barplot')
plt.xlabel('x')
plt.ylabel('y')
plt.xticks([1, 2, 3])
plt.yticks([10, 20, 30, 40])
plt.show()
plt.show()
