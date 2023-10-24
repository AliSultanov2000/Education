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

video_path = r"C:\Users\1NR_Operator_33\Downloads\Поток машин на ТТК (Москва), весна-лето 2018.mp4"  

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
