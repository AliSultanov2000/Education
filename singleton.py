class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance



results = model.train(
   data='custom_data.yaml',  # Path to the YAML file
   imgsz=640,  # Image resize
   epochs=20,  # The number of epochs
   batch=8,  # The number of batch during train
   name='yolov8_gun_detection'
)
