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
