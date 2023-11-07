class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance



def image_detection(image_path: str) -> None:
    """Run inference and plot the result for image data"""
                           
    results = model.predict(image_path, save=True)  # Results list
    
    # Show the results
    for result in results:
        im_array = result.plot()  # Plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
        im.show()  # Show image


# Test
image_detection(r"D:\Software\Снимок11.PNG")
