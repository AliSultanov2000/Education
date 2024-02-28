class RandomForestClassifier:

    def __init__(self, n_estimators=100, max_depth=None, random_state=None):
        # Конструктор класса, устанавливающий параметры модели
        self.n_estimators = n_estimators      # Количество деревьев в лесу
        self.max_depth = max_depth            # Максимальная глубина деревьев
        self.random_state = random_state      # Случайное начальное состояние для генератора случайных чисел
        self.estimators = []                  # Список для хранения деревьев
    

    def fit(self, X, y):
        # Метод для обучения модели на тренировочных данных X и метках y
        rng = np.random.default_rng(self.random_state)  # Инициализация генератора случайных чисел
        for _ in range(self.n_estimators):
            # Использование Bootstrap Aggregating для случайного выбора объектов для текущего дерева
            idxs = rng.choice(X.shape[0], X.shape[0])
            X_subset, y_subset = X[idxs], y[idxs]
            
            # Создание и обучение дерева решений с заданными параметрами
            clf = DecisionTree(max_depth=self.max_depth)
            clf.fit(X_subset, y_subset)
            self.estimators.append(clf)  # Добавление обученного дерева в список
    

    def predict(self, X):
        # Метод для предсказания меток на новых данных X
        y_pred = []
        for i in range(len(X)):
            votes = {}  # Словарь для подсчета голосов деревьев за каждый класс
            for clf in self.estimators:
                pred = clf.predict([X[i]])[0]  # Предсказание метки на текущем дереве
                if pred not in votes:
                    votes[pred] = 1
                else:
                    votes[pred] += 1
            y_pred.append(max(votes, key=votes.get))  # Выбор метки с наибольшим количеством голосов
        return np.array(y_pred)  # Возвращение предсказанных меток в виде массива numpy
