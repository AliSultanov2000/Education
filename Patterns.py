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



from sklearn.model_selection import validation_curve, learning_curve, KFold, ValidationCurveDisplay, LearningCurveDisplay
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.svm import SVC

# Train test split
X, y = load_iris(return_X_y=True)
X_train, X_Test, y_train, y_test = train_test_split(X, y, shuffle=True, random_state=50)

# Set param_range
param_range = np.logspace(-7, 3, 3)

# Cross-validation
kf = KFold(n_splits=5, shuffle=True, random_state=50)

# load model
classifier = SVC(kernel="linear")
