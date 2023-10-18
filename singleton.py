class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance


    
# ИСПОЛЬЗОВАНИЕ def в Pipeline 
# ВАЖНО 1: def в Pipeline следует использовать только для этапов трансформирования (где нету обучения fit, fit_transform)
# ВАЖНО 2: При использовании кастомной функции def, ф-я заворачивается в ООП FunctionTransformer класс, где имеются методы fit, fit_transform и тд, эти методы классы служат как "заглушка", чтобы конвейер смог и далее работать безотказно! 
# ВАЖНО 3: функция должна обязательно что-то return-ить
# ВАЖНО 4: Внутри ф-ии аргумент обзываем как X, y не надо вообще указывать в аргументах (в отличие от ООП, где надо явно прописывать y=None) - но если хочется, то можно, чтобы стандартизировать код
# ВАЖНО 5: Если в кастомную функцию хотим добавить инверсивную функцию, то при обёртке необходимо явно указать эту инверсивную функцию, иначе инверсия работать не будет (ошибки тоже не будет!)




		idxs = cv2.dnn.NMSBoxes(predict['boxes'], predict['conf'], 0.5, 0.3)

		if len(idxs) > 0:
			for i in idxs.flatten():
				(x, y) = (predict['boxes'][i][0], predict['boxes'][i][1])
				(w, h) = (predict['boxes'][i][2], predict['boxes'][i][3])
		
				color = colors[i]
				image = cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
				text = predict['label'][i] + "({:.2f})".format(predict['conf'][i])
				image = cv2.putText(image, text, (x+2, y+10), cv2.FONT_HERSHEY_PLAIN, 0.8, color, 1)
		return image


	def detect_image(self, img_path):
		"""Функция детекции военных объектов на изображении"""
		layer_name = self.get_layer_name()
		image = cv2.imread(img_path)
		Outputs = self.detect_object(image, layer_name)
		boxes, confidences, label = self.get_boxes(Outputs, image)
		predict = {
				'boxes' : boxes,
				'conf'	: confidences,
				'label'	: label
		}
		colors = np.random.uniform(0, 255, size=(len(self.Object), 3))
		result = self.draw_box(image, predict, colors)
		filename = get_predict_name(self.out_dir, 'jpg')
		cv2.imwrite(filename, result, [cv2.IMWRITE_JPEG_QUALITY, 100])

		outfile_name = os.path.basename(filename)
		print('Image file finished.')
		return outfile_name
	
