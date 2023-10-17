class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance


    
# ИСПОЛЬЗОВАНИЕ def в Pipeline 
# ВАЖНО 1: def в Pipeline следует использовать только для этапов трансформирования (где нету обучения fit, fit_transform)
# ВАЖНО 2: При использовании кастомной функции def, ф-я заворачивается в ООП FunctionTransformer класс, где имеются методы fit, fit_transform и тд, эти методы классы служат как "заглушка", чтобы конвейер смог и далее работать безотказно! 
# ВАЖНО 3: функция должна обязательно что-то return-ить
# ВАЖНО 4: Внутри ф-ии аргумент обзываем как X, y не надо вообще указывать в аргументах (в отличие от ООП, где надо явно прописывать y=None) - но если хочется, то можно, чтобы стандартизировать код
# ВАЖНО 5: Если в кастомную функцию хотим добавить инверсивную функцию, то при обёртке необходимо явно указать эту инверсивную функцию, иначе инверсия работать не будет (ошибки тоже не будет!)



"""
    Модуль для запуска локального сервера, в котором будет развёрнута модель YoLo для детекции военных объектов.
    Деплой модели пока что на Flask, в перспективе - Django.
"""

from flask import Flask
import os
import sys
from flask_cors import CORS
from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'loginflask'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/loginflask'
app.config['SECRET_KEY'] = 'detection-system'

app.secret_key = os.urandom(24)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

import views

if __name__ == "__main__":
    app.run(debug=True)

# os.system("clear-cache.sh")
