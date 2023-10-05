class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance


    



# StandardScaler
from sklearn.preprocessing import StandardScaler

s_train_data = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]], dtype='int8')
s_test_data = np.array([[1, 2, 3]])

scaler = StandardScaler()  # Создаём объект класса 

scaler.fit(s_train_data)  # Обучение. На этом этапе вычисялем статистики. ПРИ ЭТОМ САМИ ДАННЫЕ НЕ МЕНЯЮТСЯ

print(scaler.transform(s_test_data))  # Преобразование тестовых данных

# MinMaxScaler (RobustScaler по аналогии)
from sklearn.preprocessing import MinMaxScaler

mms_train_data = np.array([[13430, 45532, 1437], [14345, 434243, 1843], [17, 32434, 64436]], dtype='int8')
mms_test_data = np.array([[113, 654, 313]])

mms = MinMaxScaler()  # Создаём объект класса

mms.fit(mms_train_data)  # Обучение. На этом этапе вычисляем статистики. ПРИ ЭТОМ САМИ ДАННЫЕ НЕ МЕНЯЮТСЯ

print(mms.transform(mms_test_data))  # Преобразование тестовых данных







