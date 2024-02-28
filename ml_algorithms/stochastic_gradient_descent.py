def stochastic_gradient_descent(learning_rate=0.1, eps=0.0001,  max_iter=3500):
    """
       Запуск стохастического градиентного спуска для обучения модели линейной регрессии.
       На каждой итерации считаем ошибку, градиент функции потерь на всём обучающем X_train, y_train.
       Функцией потерь является MSE. Важно делать перемешивание данных (рандом) на каждой итерации
    """

    iter_list = []  
    cost_list = []  
    total_samples = X_train.shape[0]  # Общее кол-во объектов в X_train 
    number_of_features = X_train.shape[1]  # Количество признаков в датасете
    weights = np.zeros(number_of_features)

    next_weights = weights
    for iter in range(max_iter):
        cur_weights = next_weights   

        # Выбор случайного индекса из диапазона
        random_index = np.random.randint(0, total_samples - 1)
        sample_x, sample_y = X_train[random_index], y_train[random_index]
        # Делаем predict
        y_pred = np.dot(cur_weights, sample_x.T)
        # Вычисление функции потерь
        error = np.square(sample_y - y_pred)
        # Вычисляем вектор-градиент функции потерь по весам
        gradients = - (2 / total_samples) * (sample_x.T.dot(sample_y - y_pred))
        # Находим вектор следующих весов по ф-ле град.спуска
        next_weights = cur_weights - learning_rate * gradients

        print(f"Итерация: {iter}")
        print(f"Текущая точка {cur_weights} | Следующая точка {next_weights}")
        print(f"Ошибка: {error}")
        print("--------------------------------------------------------")

        # Сохранение результатов в списки
        iter_list.append(iter)
        cost_list.append(error)
    
        # Если ничего не меняется, то останавливаем обучение. Берём норму по всем векторам
        if np.linalg.norm(cur_weights - next_weights, ord=2) <= eps:
            print('Остановка обучения. Изменение весов меньше eps')
            break
    
    print(f'Найденные веса, обеспечивающие минимум функции потерь: {cur_weights}')
    return iter_list, cost_list
