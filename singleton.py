class Human:
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args, **kwargs):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance


# Добавить остальные паттерные проектирования которые я знаю, а именно:
# Фабрика;
# Строитель;
# Фасад;
# Адаптер;
