class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance



try:
    model = YOLO('venv/Lib/site-packages/ultralytics/yolov8n.pt')  # ---> Модель скачал вручную в папку ultralytics
    # model = YOLO('yolov8n.pt')  # ---> Для загрузки модели из GitHub репозитория моделей YOLO
    print('Модель YOLO успешна загружена')
except Exception:
    print('Возникла ошибка при загрузке модели')

# Run inference on an image
results = model.predict(r"C:\Users\1NR_Operator_33\Desktop\754598754008015.jpeg")  # results list

# Show the results
for r in results:
    im_array = r.plot()  # Plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image
