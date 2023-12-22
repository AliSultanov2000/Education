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


class LogisticRegression:
    """Example of implementation logistic regression"""

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
        return 1 / 1 + np.exp(-z)
        

    def predict(self, X: np.array):
        probabilities = self.predict_proba(X)
        return np.fromiter((1 if probability > 0.5 else 0 for probability in probabilities), dtype='int8')


    def fit(self, X: np.array, y: np.array):

        n_objects = X.shape[0]
        n_features = X.shape[1]
        self._weights = np.zeros(n_features, dtype='int8')

        self.next_weights = self._weights        
        for iter in range(self.max_iter):
            self.current_weights = self.next_weights
            # Get predict proba
            y_pred_pr = self.predict_proba(X)
            # Logloss calculation
            # logloss = - np.sum(y * np.log(y_pred_pr + 1e-9) + (1 - y) * np.log(1 - y_pred_pr +  1e-9)) / n_objects
            logloss = - (1 / n_objects) * np.sum(y * np.log(y_pred_pr) + (1 - y) * np.log(1 - y_pred_pr))

            # Get predict
            y_pred = self.predict(X) 
            # Gradients
            gradients = X.T @ (y - y_pred)
            # Weights updation
            self.next_weights = self.current_weights - self.learning_step * gradients

            # Stop when the required degree of accuracy is reached
            print(f"Iteration: {iter}")
            print(f"Current point {self.current_weights} | Next point {self.next_weights}")
            print(f"Logloss {logloss}")
            print("--------------------------------------------------------")

            # If weights updation - small then exit from the loop
            difference_weights_norm = np.linalg.norm(self.next_weights  - self.current_weights, ord=2)
            if difference_weights_norm <= self.epsilon: 
                break
        
        print(f'Found weights that provide a minimum loss function: {self.current_weights}')
        # Saving weights

        

lr = LogisticRegression(100, 0.1, 0.001)
lr.fit(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), np.array([1, 2, 3]))

estimators = [
     ('rf', RandomForestClassifier(n_estimators=10, random_state=42))
     ('svr', make_pipeline(StandardScaler(),
                           LinearSVC(dual="auto", random_state=42)))
             ]


skfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

clf = StackingClassifier(estimators=estimators, final_estimator=LogisticRegression(), cv=skfold)

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

clf.fit(X_train, y_train)

# Check the results on train, test
print(f'Metric on train: {clf.score(X_train, y_train)}')
print(f'Metric on test: {clf.score(X_test, y_test)}')

def objective(trial: optuna.Trial):
    # list of hyperparameters for optimization (CatBoostClassifier)
    param_distribution = {
        "colsample_bylevel": trial.suggest_float("colsample_bylevel", 0.01, 0.1),
        "depth": trial.suggest_int("depth", 1, 12),
        "boosting_type": trial.suggest_categorical("boosting_type", ["Ordered", "Plain"]),
        "bootstrap_type": trial.suggest_categorical("bootstrap_type", ["Bayesian", "Bernoulli", "MVS"]),
                         }

    # Smart idea! 
    if param_distribution["bootstrap_type"] == "Bayesian":
        param_distribution["bagging_temperature"] = trial.suggest_float("bagging_temperature", 0, 10)
    elif param_distribution["bootstrap_type"] == "Bernoulli":
        param_distribution["subsample"] = trial.suggest_float("subsample", 0.1, 1)

    # The model (Here we can use Pipeline, custom classes, def function)
    model = CatBoostClassifier(**param_distribution, loss_function='MultiClass', verbose=False)

    # Cross validation
    kf = KFold(n_splits=5, shuffle=True, random_state=50)  # Set fold strategy
    cv_scores = cross_val_score(model, X_train, y_train, cv=kf, scoring='f1_macro')  # Metric results for all folds
    score = np.mean(cv_scores)  # Mean for all folds 
    std = np.std(cv_scores)  # Std by all folds

    # User attribute
    trial.set_user_attr("score", score)
    trial.set_user_attr("std", std)

    # Return the metric 
    return score


# Sampler: TPE
sampler = optuna.samplers.TPESampler(seed=42)
# DB Storage
storage_url = "sqlite:///example.db"
# study_name
study_name = "catt_optimization"
# Pruner using 
pruner = SuccessiveHalvingPruner(min_resource=1, reduction_factor=2, min_early_stopping_rate=0)
#Create a study 
study = optuna.create_study(sampler=sampler,
                            direction='maximize',
                            storage=storage_url,
                            load_if_exists=True,
                            study_name=study_name,
                            pruner=pruner)


# START! 
study.optimize(objective,   # What we have to optimize
               n_trials=20,  # The number of trials 
               timeout=5000)  # The time of optimizing 

# Garbage collector 
gc.collect()
