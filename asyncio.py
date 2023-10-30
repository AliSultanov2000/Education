# Асинхронное программирование — концепция программирования, при которой результат выполнения ассинхронной функции доступен спустя некоторое время
# в виде асинхронного (нарушающего стандартный порядок выполнения) вызова. Запуск длительных операций происходит без ожидания их завершения и не блокирует дальнейшее выполнение программы.
# АССИНХРОННОЕ ПРОГРАММИРОВАНИЕ НЕ ПОДРАЗУМЕВАЕТ ПОД СОБОЙ ПАРАЛЛЕЛЬНОЕ ВЫЧИСЛЕНИЕ!!!


# Ассинхронное программирование применяется для оптимизации выполнения высоконагруженных сервисов с частым ожиданием чего-либо.
# Например, когда мобильное приложение запрашивает и загружает данные с сервера, экран смартфона демонстрирует активность программы — анимированную
# заставку или раздел помощи. Основной поток приложения при этом находится в режиме ожидания данных, загружаемых с удаленного сервера.
# АССИНХРОННОСТЬ в программировании применяется для следующих задач:
# 1) Запрос к базе данных
# 2) Запрос к серверу
# 3) Ожидание ввода/вывода пользователя

# АССИНХРОННОСТЬ ЧАЩЕ ВСЕГО ПРИМЕНЯЕТСЯ ПРИ РАБОТЕ С ВЕБОМ!

# Общее время выполнения ассинхронной программы ограничивается временем выполнения самой долгой задачи.

# В Python ассинхронность реализуется за счёт модуля asyncio
# Ассинхронность добавляется за счёт ключевых слов async, await.
# async говорит интерпретатору, что эта функция ассинхронная
# await говорит интерпретатору, иди дальше к другим функциям, я посплю немного

# Ключевыми сущностями в ассинхронном программировании являются корутины и задачи.

# КОРУТИНЫ - разновидность генератора. Корутина дает интерпретатору возможность возобновить базовую функцию, которая была приостановлена в месте размещения ключевого слова await.
# Если в функции есть async, await, то эта функция - корутина. Причем корутина это именно вызов ассинхронной функции f() - по аналогии с генератором
# ЗАДАЧИ в ассинхронном программировании необходимы, чтобы в них оборачивать КОРУТИНЫ
# Задачи — это "ракеты-носители" для ассинхронного запуска "боеголовок"-функций.

# !!!! 1 ВАЖНО: Ассинхронный запуск корутин будет соответствовать порядку следования создания task-ов в main, т.е. task1 = create_task(), task2 = create_task() и тд,  а не await task1, await task2
# !!!! 2 ВАЖНО: В ассинхронной программе всегда нужна верхнеуровневая ассинхронная функция async main()

# asyncio.sleep() - не блокирует интерпретатор, как стандартный sleep()
# Ассинхронная программа на Python запускается при помощи команды asyncio.run(main())
# В asyncio.run нужно передавать асинхронную функцию main() с await на задачи, а не на корутины. Иначе не взлетит. То есть работать-то будет, но сугубо последовательно, без всякой конкурентности.

# ДОПОЛНИТЕЛЬНО:
# 1) Для работы с вебом есть библиотека aiohttp
# 2) Для работы с контекстным менеджером есть конструкция async with...


# Пример 1: База ассинхронного программирования

import asyncio

# Ассинхронная функция 1
async def func1(x1: int) -> None:
    """Ассинхронная функция для вычисления квадрата числа"""
    print('Начало работы функции func1')
    await asyncio.sleep(5)
    print(f'Результат вычисления квадрата числа {x1}: {x1 ** 2}')

# Ассинхронная фунция 2
async def func2(x2: int) -> None:
    """Ассинхронная функция для вычисления куба числа"""
    print('Начало работы функции func2')
    await asyncio.sleep(3)
    print(f'Результат вычисления куба числа {x2}: {x2 ** 3}')

# Главная ассинхронная функция для запуска
async def main() -> None:
    task1 = asyncio.create_task(func1(5))  # type(task1): '_asyncio.Task
    task2 = asyncio.create_task(func2(5))

    await task1
    await task2

# Запуск ассинхронной программы
if __name__ == '__main__':
    asyncio.run(main())



# А может ли асинхронная функция не просто что-то делать внутри себя (например, запрашивать и выводить в консоль погоду), но и возвращать результат return,
# чтобы дальнейшей обработкой занималась функция верхнего уровня main()?
# Нет ничего проще. Только в этом случае для группового запуска задач необходимо использовать уже не await внутри main(), а функцию asyncio.gather (см. Пример 2)

# Пример 2: Ассинхронность с return внутри корутин

import asyncio

# Ассинхронная функция 1
async def func1(x1: int) -> str:
    """Ассинхронная функция для вычисления квадрата числа"""
    print('Начало работы функции func1')
    await asyncio.sleep(5)  # Ассинхронная остановка на 5 секунд
    return f'Результат вычисления квадрата числа {x1}: {x1 ** 2}'

# Ассинхронная функция 2
async def func2(x2: int) -> str:
    """Ассинхронная функция для вычисления куба числа"""
    print('Начало работы функции func2')
    await asyncio.sleep(3)  # Ассинхронная остановка на 3 секунды
    return f'Результат вычисления куба числа {x2}: {x2 ** 3}'

# Главная ассинхронная функция для запуска 
async def main() -> None:
    task1 = asyncio.create_task(func1(5))  # type(task1): '_asyncio.Task
    task2 = asyncio.create_task(func2(5))
    tasks = [task2, task1]   # Дальнейший порядок обработки тасков хранится в этом списке. Сначала будет обработано task2
    results = await asyncio.gather(*tasks)  # type(results): list
    print(results)

# Запуск ассинхронной программы
if __name__ == '__main__':
    asyncio.run(main())


# preprocessor на других данных
# Как видим, признаковое пр-во не увеличилось (OneHotEncoder +)
preprocessor.transform([[20, 650, 'White', 'male']])


# Пайплайн для prod-a. Сделан на основе preprocessor-а (ColumnTransform)
final_pipe = Pipeline([('preprocessor', preprocessor),  # Completely preprocessing num, text
                       ('model', lr)])  # Final estimator - LogisticRegression


# Посмотрим final_pipe
final_pipe


# Обучаем preprocessor, обучаем log-reg
final_pipe.fit(X_train, y_train)


# Запускаем на оценку score (transform, а в конце у estimator-а отрабатывает score)
final_pipe.score(X_test, y_test)

from sklearn.linear_model import LogisticRegression


# Определяем данные
X = pd.DataFrame({'age': [10, 20, 30, 40, 50, 60], 'balance': [400, 600, 800, 1000, 1200, 1400], 'kernel': ['White', 'Black', 'Green', 'Yellow', 'White', 'Black'], 'sex': ['male', 'female', 'male', 'female', 'male', 'female']})
y = [1, 1, 1, 0, 0, 0]


# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=42) 


# Определяем модель для предсказания
lr = LogisticRegression()


# Ищем индексы столбцов с числами
num_columns = X.select_dtypes('int').columns
num_columns_indexes = X.columns.get_indexer(num_columns)


# Ищем индексы столбцов с текстом
text_columns = X.select_dtypes('object').columns
text_columns_indexes = X.columns.get_indexer(text_columns)


# Функция для работы с int
def meta_num(X, y=None):
    """Функция для тестирования работы с num"""
    X[X.nonzero()] = X[X.nonzero()] + 100
    return X

transs1 = FunctionTransformer(meta_num)


# Функция для работы с text
def meta_text(X, y=None):
    """Функция для тестирования работы с text"""
    X[X.nonzero()] = X[X.nonzero()] + 1
    return X 

transs2 = FunctionTransformer(meta_text)


# Создаём внутренний пайплайн для int
num_pipe = Pipeline([('scaler', StandardScaler()), ('meta_add1', transs1)])


# Создаём внутренний пайплайн для text
text_pipe = Pipeline([('ohe', OneHotEncoder(handle_unknown="ignore")), ('meta_add2', transs2)])


# Создаём ColumnTransformer
preprocessor = ColumnTransformer([('tr1', num_pipe, num_columns_indexes),
                        ('tr2', text_pipe, text_columns_indexes)])


# Посмотрим на preprocessor(ColumnTransformer)
preprocessor

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer


X = pd.DataFrame({'age': [10, 20, 30, 40], 'balance': [400, 600, 800, 1000], 'kernel': ['White', 'Black', 'Green', 'Yellow'], 'sex': ['male', 'female', 'male', 'female']})



def change_num1(X: pd.DataFrame, y=None):
    """Функция для работы с колонкой age"""
    return X + 10 

def change_num2(X: pd.DataFrame, y=None):
    """Функция для работы с колонкой balance"""
    return X - 100


trans1 = FunctionTransformer(change_num1)
trans2= FunctionTransformer(change_num2)


ct = ColumnTransformer([("tr1", trans1, ["age"]), ("tr2", trans2, ["balance"]), ("tr3", OneHotEncoder(), ['kernel', 'sex'])])
ct.fit_transform(X)

# ГИПЕРВАЖНО: доступ к гиперпараметрам конвейера: --- ЭТО ВАЖНО ПРИ ПОИСКЕ ПО СЕТКЕ!!!
# 1) Пишем сначала полное название шага конвейера
# 2) Далее ставим __ 
# 3) Пишем название гиперпараметра

pipe1.set_params(clf__C=10)
