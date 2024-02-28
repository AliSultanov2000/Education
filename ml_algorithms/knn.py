class KNeighborsClassifier:
    """Класс для реализации алгоритма KNN для задачи классификации объектов"""

    def __init__(self, n_neighbors=5):
        self.n_neighbors = n_neighbors
    
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
    
    def predict(self, X):
        y_pred = np.array([])
        # Пробегаемся по всем элементам
        for i in range(len(X)):
            # Вычисляем евклидово расстояние от объекта до всех объектов из train-a
            distances = np.sqrt(np.sum((self.X_train - X[i]) ** 2, axis=1))
            # Находим индексы n_neighbors объектов
            nearest_indices = np.argsort(distances)[:self.n_neighbors]
            # Находим метки n_neighbors объектов
            nearest_labels = self.y_train[nearest_indices]
            # Вычисляем класс
            label = np.bincount(nearest_labels).argmax()
            # Запоминаем предикт по текущему объекту
            y_pred = np.append(y_pred, label)
            
        return np.array(y_pred)
