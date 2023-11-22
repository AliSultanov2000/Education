class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance

# Example data
X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])
y = np.array([1, 2, 3, 4])
kf = KFold(n_splits=4)

# Split ---> train_idx, test_idx. Обращаться к самим блокам можно по этим индексам
for i, (train_idx, test_idx) in enumerate(kf.split(X)):
    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]
    print(f'Split: {i}')
    print("TRAIN idxs:", train_idx, "TEST idxs:", test_idx)
    print(f'X train for all folds:\n {X_train}')
    print(f'y_train for all folds:\n {y_train}\n')
