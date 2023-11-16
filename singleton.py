class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance



# plt.rcParamsDefault.copy()  # Просмотр существующих rcParams

matplotlib_params = {
    'legend.fontsize': 'medium',
    'lines.linewidth': 2,
    # 'axes.grid': False,
    'xtick.labelsize': 13,
    'ytick.labelsize': 13,
    'axes.labelsize': 14,
    'axes.titlesize': 14,
    "legend.fancybox": True,
    'legend.loc': 'best'
}

pylab.rcParams.update(matplotlib_params)

fig, ax = plt.subplots()
ax.set(title='Example of graph', xlabel='x', ylabel='y')
ax.plot(x, y, label='quadratic function')
ax.legend();
