class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance


x = range(11)  
y1 = [i for i in x]  
y2 = [i ** 2 for i in x]

fig, axs = plt.subplots(1, 2, figsize=(12, 7))
axs[0].plot(x, y1, label='linear function', marker='*', markersize=4, color='red')

axs[0].set_xlabel('Linear', fontsize=14)
axs[0].set_ylabel('Value', fontsize=14)
axs[0].set_title('First graph')

axs[1].plot(x, y2, label='quadratic function', marker='o', markersize=4, color='green')

axs[1].set_xlabel('Quadratic', fontsize=14)
axs[1].set_ylabel('Value', fontsize=14)
axs[1].set_title('Second graph')

plt.show()
