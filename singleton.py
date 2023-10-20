class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance


from sklearn.feature_extraction.text import CountVectorizer 

count_vectorizer1 = CountVectorizer()  # Реализует концепцию мешка слов
vectors1 = count_vectorizer1.fit_transform(train_docs)  # Сначала запускается метод fit, а далее запускается метод transform, который return-ит вектор для каждого текста; При вызове fit получается вокабуляр слов
vectors1

# Посмотрим вокабуляр слов (на этих словах обучались). Индекс означает порядок слова в df 
count_vectorizer1.vocabulary_


# Пример predict-а, в нижних примерах можно также реализовать!
predict = count_vectorizer1.transform(['Sun is sweet'])
print(type(predict))  # Также sparse_matrix
print(predict.toarray())
