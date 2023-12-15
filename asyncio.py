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

class YoloTracker(YoloModel):
    """Класс YOLOv8 для задачи трекинга объектов"""

    def __init__(self, model_path):
        super().__init__(model_path)


    def image_tracking(self, image_path: str) -> None: 
        """Предсказание модели на изображении"""
        
        # Список с результатами
        results = self.model.track(image_path, persist=True)
        # Отображение на экран
        annotated_frame = self._box_plotting(results)
        cv2.imshow("Sharp eye", annotated_frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
 
        
    def stream_tracking(self, video_path: str, cls_display: Display) -> None: 
        """Предсказание модели на видеопотоке"""

        # Открытие видео файла 
        cap = cv2.VideoCapture(video_path)
        frame_count = 0
        assert cap.isOpened()

        # Цикл по видео фрейму
        while cap.isOpened():
            cls_display.start_time = time()
            # Считывание фрейма из видео
            success, frame = cap.read()

            if success:
                # Запуск YOLOv8 трекера
                results = self.model.track(frame, persist=True)
                # Отображение на экране box-ов
                annotated_frame = self._box_plotting(results) 

                # Вывод времени работы, fps, эмблемы на дисплей
                cls_display.working_time_display(annotated_frame)
                cls_display.fps_display(annotated_frame)
                cls_display.logotype_display(annotated_frame)
                cls_display.target_aiming_display(annotated_frame, 640, 360)  # Координаты x_center, y_center 

                # Вывод кадра на экран
                cv2.imshow('Sharp eye', annotated_frame)
                frame_count += 1
                # Остановка цикла при нажатии "q"
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            else:
                # Остановка цикла, если видео закончено
                break
        
        # Закрытие видеопотока 
        cap.release()
        cv2.destroyAllWindows()



if __name__ == '__main__':
    # Cоздание экземпляра класса
    tracker = YoloTracker(r"C:\Users\1NR_Operator_33\runs\detect\yolov8_tank_detection42\weights\best.pt")
    # tracker.model.names[0] = 'Танк'
    print(f'Загружена модель: {tracker.model_path}')
    print(f'Используемый девайс: {tracker.device}')


    # Запуск на трекиг видеопотока
    tracker.stream_tracking(r"C:\Users\1NR_Operator_33\Downloads\танк Т90м Прорыв лучший танк в мире в бою.mp4", Display())


class YoloModel:
    """Базовый класс для работы с YOLOv8"""

    def __init__(self, model_path):

        self.device = 'cuda' if is_available() else 'cpu'
        self.model_path = model_path
        self.model = self.load_model()
        self.CLASS_NAMES_DICT = self.model.names

        
    def load_model(self):
        """Загрузка модели YOLOv8"""

        model = YOLO(self.model_path)
        model = model.to(device='cpu')
        model.fuse()
        return model


    def train_model(self, data, imgsz, epochs, batch, name):
        """Тренировка модели YOLOv8 для задачи трекинга"""

        self.model.train(
        data=data,  # Путь до YAML файла
        name=name,  # Название модели, которая сохранится 
        imgsz=imgsz,  
        epochs=epochs,  
        batch=batch)
    

    def test_model(self):
        """Запуск на тестирование модели YOLOv8"""
        # self.model.val()


    def _box_plotting(self, results):
        """Отображение на экране box-а c распознанными объектами"""
    
        # Получение всех боксов
        boxes = results[0].boxes.xywh.cpu()
        # Визуализация результата на фрейме
        annotated_frame = results[0].plot()
        # Отрисовка бокса с указанием id трека 
        for box in boxes:
            x, y, w, h = box
            x, y, w, h = int(x), int(y), int(w), int(h)
            # Отрисовка центров для Bounding Boxes
            cv2.drawMarker(annotated_frame, (x, y), (0, 0, 255), cv2.MARKER_CROSS, 15, 2)

        return annotated_frame 

class Display:
    """Класс для отображения дополнительной информации о работе трекера на экран"""
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.START_TIME = time()


    def working_time_display(self, im0) -> None: 
        """Отображение на экран времени работы"""
        self.CURRENT_TIME = time()
        working_time = str(datetime.timedelta(seconds=round(self.CURRENT_TIME - self.START_TIME)))
        cv2.putText(im0, f'Время работы: {working_time}', (950, 25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)


    def fps_display(self, im0) -> None:
        """Отображение на экран FPS"""
        self.end_time = time()
        fps = 1 / np.round(self.end_time - self.start_time, 2)
        text = f'FPS: {int(fps)}'
        cv2.putText(im0, text, (1163, 60), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
    

    def target_aiming_display(self, im0, x_center: int, y_center: int) -> None:
        """Указатель на цель при отработке трекера"""
        
        # Отображение линии наведения
        gap = int(x_center // 32)
        line_length = int(x_center // 11)
        cv2.circle(im0, (x_center, y_center), 5, (0, 255, 0), -1)
        cv2.line(im0, (x_center - gap - line_length, y_center), (x_center - gap, y_center), (0, 255, 0), 2)
        cv2.line(im0, (x_center + gap, y_center), (x_center + gap + line_length, y_center), (0, 255, 0), 2)  
        cv2.line(im0, (x_center, y_center + gap), (x_center, y_center + gap + line_length // 2),  (0, 255, 0), 2)

        # Отображение прямоугольника наведения
        pointer_box_w = int(x_center // 3.2)  
        pointer_box_h = int(y_center / 2.4)  
        cvzone.cornerRect(im0, (x_center - pointer_box_w // 2, y_center - pointer_box_h // 2, pointer_box_w, pointer_box_h), rt=0)
    

    def logotype_display(self, im0) -> None:
        """Отображение логотипа. Логотип должен быть только в PNG"""
        
        img_front = cv2.imread(r"D:\russian_flag.PNG", cv2.IMREAD_UNCHANGED)
        img_front = cv2.resize(img_front, (64, 48))
        cvzone.overlayPNG(im0, img_front, pos=[10, 10])


