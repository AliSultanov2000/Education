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


class LogisticRegression: 
    def __init__(self, max_iter: int, learning_step: float,  epsilon: float,  treshold=0.5):
        self.max_iter = max_iter
        self.learning_step = learning_step
        self.epsilon = epsilon
        self.treshold = treshold

        self._weights = None
        self.next_weights = None
        self.current_weights = None

        
    def predict_proba(self, X: np.array):
        z = (X @ self.current_weights)
        return 1 / np.exp(-z)
        

    def predict(self, X: np.array):
        probabilities = self.predict_proba(X)
        return np.fromiter((1 if probability > 0.5 else 0 for probability in probabilities), dtype='int8')


    def fit(self, X: np.array, y: np.array):
        n_objects = X.shape[0]
        n_features = X.shape[1]
        self._weights = np.zeros(n_features)

        self.next_weights = self._weights        
        for iter in range(self.max_iter):
            self.current_weights = self.next_weights
            # Get predict proba
            y_pred_pr = self.predict_proba(X)
            # Logloss calculation
            logloss = - np.sum(y * np.log(y_pred_pr + 1e-9) + (1 - y) * np.log(1 - y_pred_pr +  1e-9)) / n_objects

            # Get predict
            y_pred = self.predict(X) 
            # Gradients
            gradients = X.T @ (y - y_pred)
            # Weights updation
            self.next_weights = self.current_weights - self.learning_step * gradients

            # Остановка когда достигнута необходимая степень точности
            print(f"Итерация: {iter}")
            print(f"Текущая точка {self.current_weights} | Следующая точка {self.next_weights}")
            print(f"Logloss {logloss}")
            print("--------------------------------------------------------")

            # If weights updation - small then exit from loop
            difference_weights_norm = np.linalg.norm(self.next_weights  - self.current_weights, ord=2)
            if difference_weights_norm <= self.epsilon: 
                break
        
        print(f'Найденные веса, обеспечивающие минимум функции потерь: {self.current_weights}')
        # Сохранение весов в классе
        

lr = LogisticRegression(100, 0.1, 0.001)
lr.fit(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), np.array([1, 2, 3]))
