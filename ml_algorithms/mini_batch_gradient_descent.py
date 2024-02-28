def mini_batch_gradient_descent(learning_rate=0.1, eps=0.0001,  epochs=100, batch_size=10):
    """
       Запуск пакетного градиентного спуска для обучения модели линейной регрессии.
       Необходимо пробегаться двумя циклами: по эпохам и по бачам.
       На каждой итерации считаем ошибку, градиент функции потерь на всём обучающем X_train, y_train.
       Функцией потерь является MSE. Важно делать перемешивание данных (рандом) на каждой итерации.
    """

    epoch_list = [] 
    mse_list = []
    stop_learning = False

    total_samples = X_train.shape[0] # Количество объектов в X_train
    number_of_features = X_train.shape[1]  # Количество признаков в датасете
    
    if batch_size > total_samples: 
        raise IndexError('Размер batch-a превышает количество объектов в выборке train')
    
    weights = np.ones((number_of_features))
    next_weights = weights
    for epoch in range(epochs): 
        # Делеаем перемешивание для всего train на каждой итерации
        random_indices = np.random.permutation(total_samples)  # Все перемешанные индексы train-a 
        X_tmp, y_tmp = X_train[random_indices], y_train[random_indices]  # Все перемешанные объекты train-a
        # Проходимся по всем бачам в эпохе
        for batch_index in range(0, total_samples, batch_size):
            cur_weights = next_weights
            # Определяем батч
            X_batch, y_batch = X_tmp[batch_index: batch_index + batch_size], y_tmp[batch_index: batch_index + batch_size]
            # Делаем predict
            y_pred = np.dot(cur_weights, X_batch.T)
            # Вычисление функции потерь
            mse_error = np.sum((y_batch - y_pred) ** 2) / len(y_batch)
            # Вычисляем вектор-градиент функции потерь по весам
            gradients = - (2 / len(X_batch)) * (X_batch.T.dot(y_batch - y_pred))
            # Находим вектор следующих весов по ф-ле град.спуска
            next_weights = cur_weights - learning_rate * gradients

            print(f"Эпоха: {epoch}; Батч: {int(batch_index / batch_size)}")
            print(f"Текущая точка {cur_weights} | Следующая точка {next_weights}")
            print(f"Ошибка: {mse_error}")
            print("--------------------------------------------------------")

            # Если ничего не меняется, то останавливаем обучение. Берём норму по всем векторам
            if np.linalg.norm(cur_weights - next_weights, ord=2) <= eps:
                print('Остановка обучения. Изменение весов меньше eps')
                stop_learning = True
                break
        
        # Сохранение результатов в списки
        epoch_list.append(epoch)  # Текущая эпоха
        mse_list.append(mse_error)  # Добавляем ошибку на последнем batch-e текущей эпохи

        if stop_learning: 
            break
        
    print(f'Найденные веса, обеспечивающие минимум функции потерь: {cur_weights}') 
    return epoch_list, mse_list
