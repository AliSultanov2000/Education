def batch_gradient_descent(learning_rate=0.1, eps=0.0001,  max_iter=100): 
    """
       Запуск градиентного спуска для обучения модели линейной регрессии.
       На каждой итерации считаем MSE, градиент функции потерь на всём обучающем X_train, y_train.
       Функцией потерь является MSE.
    """

    iter_list = []  
    mse_list = []
    weights = np.zeros(X_train.shape[1])
    next_weights = weights
    # Запускаем цикл градиентного спуска (обучения линейной регрессии)
    for iter in range(max_iter):
        cur_weights = next_weights

        # Делаем predict 
        y_pred = X_train @ cur_weights
        # Вычисление функции потерь: MSE
        mse_error = np.sum((y_train - y_pred) ** 2) / len(y_train)
        # Вычисляем вектор-градиент функции потерь по весам
        gradients = 2 / len(X_train) * (y_train - y_pred) @ (-X_train)
        # Находим вектор следующих весов по ф-ле град.спуска
        next_weights = cur_weights - learning_rate * gradients

        print(f"Итерация: {iter}")
        print(f"Текущая точка {cur_weights} | Следующая точка {next_weights}")
        print(f"Ошибка: {mse_error}")
        print("--------------------------------------------------------")

        # Сохранение результатов в списки
        iter_list.append(iter)
        mse_list.append(mse_error)
    
        # Если ничего не меняется, то останавливаем обучение. Берём норму по всем векторам
        if np.linalg.norm(cur_weights - next_weights, ord=2) <= eps:
            print('Остановка обучения. Изменение весов меньше eps')
            break
    
    print(f'Найденные веса, обеспечивающие минимум функции потерь: {cur_weights}')
    return iter_list, mse_list
