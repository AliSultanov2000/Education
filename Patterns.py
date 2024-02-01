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
                cls_display.project_name_display(annotated_frame, 640, 360)
                cls_display.target_aiming_display(annotated_frame, 640, 360)  # Координаты x_center, y_center

                # Вывод кадра на экран
                cv2.imshow('YOLOv8 tracker', annotated_frame)
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
        cv2.putText(im0, f'Время работы: {working_time}', (950, 25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1, cv2.LINE_AA)


    def fps_display(self, im0) -> None:
        """Отображение на экран FPS"""
        
        self.end_time = time()
        fps = 1 / np.round(self.end_time - self.start_time, 2)
        text = f'FPS: {int(fps)}'
        cv2.putText(im0, text, (1163, 60), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
    

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


    def project_name_display(self, im0, x_center: int, y_center: int) -> None: 
        """Отображение названия трекера"""

        text = 'Трекер ВТ'
        cv2.putText(im0, text, (x_center - 50, 25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
