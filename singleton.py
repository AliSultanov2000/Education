class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance


plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(x, y1, label='linear function', marker='*', markersize=4, color='red')

plt.title('Linear function')
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(x, y2, label='quadratic function',  marker='o', markersize=4, color='green')

plt.title('Quadratic function')
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.grid()
