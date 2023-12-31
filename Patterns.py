"""
Учебный файл с реализацией основных паттернов проектирование, так как: 
   - Синглтон;
   - Адаптер;
   - Фасад; 
   - Строитель;
   - Фабрика;
   - Декоратор;
"""



class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance



class Node:
    
    def __init__(self, feature_idx=None, threshold=None, left=None, right=None, value=None):
        self.feature_idx = feature_idx    # Индекс признака, по которому разбивается вершина
        self.threshold = threshold        # Пороговое значение, по которому разбивается вершина
        self.left = left                  # Левое поддерево
        self.right = right                # Правое поддерево
        self.value = value                # Значение в листовой вершине


class DecisionTree:

    def __init__(self, min_samples_split=2, max_depth=100, n_feats=None):
        self.min_samples_split = min_samples_split   # Минимальное количество выборок, необходимых для разделения вершины
        self.max_depth = max_depth                   # Максимальная глубина дерева
        self.n_feats = n_feats                       # Количество признаков, используемых для разделения вершин
        self.root = None


    def fit(self, X, y):
        self.n_feats = X.shape[1] if not self.n_feats else min(self.n_feats, X.shape[1])
        self.root = self._grow_tree(X, y)


    def _grow_tree(self, X, y, depth=0):
        n_samples, n_features = X.shape
        n_labels = len(np.unique(y))

        # Проверяем условие остановки рекурсии
        if (depth >= self.max_depth or n_labels == 1 or n_samples < self.min_samples_split):
            leaf_value = self._most_common_label(y)
            return Node(value=leaf_value)

        feat_idxs = np.random.choice(n_features, self.n_feats, replace=False)

        # Ищем лучшее разделение признака
        best_feat, best_thresh = self._best_criteria(X, y, feat_idxs)

        # Разделяем данные и делаем рекурсивный вызов для левого и правого поддеревьев
        left_idxs, right_idxs = self._split(X[:, best_feat], best_thresh)
        left = self._grow_tree(X[left_idxs, :], y[left_idxs], depth+1)
        right = self._grow_tree(X[right_idxs, :], y[right_idxs], depth+1)

        # Возвращаем новую вершину дерева
        return Node(best_feat, best_thresh, left, right)


    def _best_criteria(self, X, y, feat_idxs):
        best_gain = -1
        split_idx, split_thresh = None, None
        for feat_idx in feat_idxs:
            X_column = X[:, feat_idx]
            thresholds = np.unique(X_column)
            for threshold in thresholds:
                gain = self._information_gain(y, X_column, threshold)
                if gain > best_gain:
                    best_gain = gain
                    split_idx = feat_idx
                    split_thresh = threshold
        return split_idx, split_thresh


    def _information_gain(self, y, X_column, split_thresh):
        # Вычисляем энтропию перед разбиением
        parent_entropy = self._entropy(y)
        # Разделяем выборки по пороговому значению
        left_idxs, right_idxs = self._split(X_column, split_thresh)
        # Если разделение не привело к изменению выборок, возвращаем нулевой информационный прирост
        if len(left_idxs) == 0 or len(right_idxs) == 0:
            return 0
        # Вычисляем энтропию после разбиения
        n = len(y)
        n_l, n_r = len(left_idxs), len(right_idxs)
        e_l, e_r = self._entropy(y[left_idxs]), self._entropy(y[right_idxs])
        child_entropy = (n_l / n) * e_l + (n_r / n) * e_r
        # Вычисляем информационный прирост
        ig = parent_entropy - child_entropy
        return ig


    def _entropy(self, y):
        # Вычисляем энтропию выборки
        _, counts = np.unique(y, return_counts=True)
        probs = counts / len(y)
        entropy = -np.sum(probs * np.log2(probs))
        return entropy


    def _split(self, X_column, split_thresh):
        # Разделяем выборки по пороговому значению
        left_idxs = np.argwhere(X_column <= split_thresh).flatten()
        right_idxs = np.argwhere(X_column > split_thresh).flatten()
        return left_idxs, right_idxs


    def _most_common_label(self, y):
        # Возвращает наиболее часто встречающееся значение в выборке
        _, counts = np.unique(y, return_counts=True)
        return max(zip(_, counts), key=lambda x: x[1])[0]


    def predict(self, X):
        # Прогнозируем метки для новых данных
        return np.array([self._traverse_tree(x, self.root) for x in X])


    def _traverse_tree(self, x, node):
        if node.value is not None:
            return node.value
        if x[node.feature_idx] <= node.threshold:
            return self._traverse_tree(x, node.left)
        else:
            return self._traverse_tree(x, node.right)


    def visualize_tree(self):
        # Создаем объект `Digraph` из библиотеки graphviz
        dot = graphviz.Digraph()

        # Внутренняя функция `add_nodes` для рекурсивного добавления узлов дерева
        def add_nodes(node):
            # Если узел содержит значение (лист), добавляем его значение в качестве метки
            # Иначе добавляем условие разбиения (порог и номер признака)
            if node.value is not None:
                label = str(node.value)
            else:
                label = "X[" + str(node.feature_idx) + "] <= " + str(node.threshold)

            # Добавляем узел в объект `Digraph`
            dot.node(str(id(node)), label)
            # Если у узла есть левый потомок, добавляем ребро и вызываем `add_nodes` для левого потомка
            if node.left is not None:
                dot.edge(str(id(node)), str(id(node.left)))
                add_nodes(node.left)
            # Если у узла есть правый потомок, добавляем ребро и вызываем `add_nodes` для правого потомка
            if node.right is not None:
                dot.edge(str(id(node)), str(id(node.right)))
                add_nodes(node.right)
        # Вызываем `add_nodes` для корневого узла дерева
        add_nodes(self.root)
        # Возвращаем объект `Digraph`
        return dot



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



class GradientBoostingRegressor: 
    
    def __init__(self, gamma=5, n_estimators=100, max_depth=6, learning_rate=0.01, random_state=10):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.learning_rate = learning_rate
        self.random_state = random_state
        self.gamma = gamma
    
    
    def loss_gradient(self, y_true, y_pred): 
        return y_true - y_pred
    

    def gamma_regul(self, tree):
        return self.gamma * tree.tree_.n_leaves
    

    def fit(self, X, y): 
        self.trees = []
        self.y_base = np.mean(y, axis=0)
        self.y_pred = self.y_base

        for _ in range(self.n_estimators):
            gradient = self.loss_gradient(y, self.y_pred)
            clf = DecisionTreeRegressor(random_state=self.random_state, max_depth=self.max_depth)
            clf.fit(X, gradient)
            self.trees.append(clf)
            self.y_pred += self.learning_rate * clf.predict(X) + self.gamma_regul(clf)

    
    def predict(self, X):
        y_composition = self.y_base + self.learning_rate * np.sum([tree.predict(X) for tree in self.trees], axis=0)  # Предикт композиции
        y_gamma = np.sum([self.gamma_regul(tree) for tree in self.trees], axis=0)                                    # Регуляризация модели
        return y_composition + y_gamma    
