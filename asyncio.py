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


def stream_detection(video_path: str) -> None:
    """Run inference and plot the result for video data"""
    
    cap = cv2.VideoCapture(video_path)

    # Loop through the video frames
    while cap.isOpened():
    # Read a frame from the video
        success, frame = cap.read()

        if success:
            # Run YOLOv8 inference on the frame
            results = model(frame)

            # Visualize the results on the frame
            annotated_frame = results[0].plot()

            # Display the annotated frame
            cv2.imshow("YOLOv8 Inference", annotated_frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            # Break the loop if the end of the video is reached
            break

    # Release the video capture object and close the display window
    cap.release()
    cv2.destroyAllWindows()


# Test
stream_detection(CONFIG_DATA['video_predict_path'])

results = model.train(
   data=CONFIG_DATA['data'],  # Path to the YAML file
   imgsz=CONFIG_DATA['imgsz'],  # Image resize
   epochs=CONFIG_DATA['epochs'],  # The number of epochs
   batch=CONFIG_DATA['batch'],  # The number of batch during train
   name=CONFIG_DATA['name']  # The name of trained model
   )

def image_detection(image_path: str) -> None:
    """Run inference and plot the result for image data"""
                           
    results = model.predict(image_path)  # Results list
    # Show the results
    for result in results:
        im_array = result.plot()  # Plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
        im.show()  # Show image


# Test
image_detection(CONFIG_DATA['image_predict_path'])


def load_config_data(data_path: str) -> dict: 
    """Функция для загрузки всех данных из конфигурационного файла yaml"""
    try:
        with open(data_path, 'r', encoding='utf8') as file:
            config_data = yaml.safe_load(file)
            return config_data
        
    except FileNotFoundError:
        print('Ошибка при загрузке конфигурационного файла')


# Загрузка всех переменных из конфигурационного файла
CONFIG_DATA = load_config_data('config.yaml')
print(CONFIG_DATA)

# pretrained_model = YOLO(CONFIG_DATA['load_path'])
