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

from spellchecker import SpellChecker

# Пример 1: через ф-ю

def spell_check(text: str):
    """Функция для устранения орфографических ошибок в тексте.
       Запускается от apply"""
    result = []
    spell = SpellChecker()
    for word in text.split():
        correct_word = spell.correction(word)
        result.append(correct_word)
    return result

#Test
text = "He how are you? i am finee"

spell_check(text)

# Пример 2: через list comprehensive
text = 'He how are you? i am finee'

[SpellChecker().correction(word) for word in text.split()]

from nltk.stem import SnowballStemmer # Стемминг


# Пример стеммера из nltk (Этот стеммер наиболее новый)
stemmer = SnowballStemmer('english')
stemmer.stem('Building')

words = 'Today was very gorgeous day! I will be in mall and buy a lot of purchases'
review = [stemmer.stem(word) for word in words.split()]
print(review)

import numpy as np

train_docs = np.array(['The sun is shining', 
                 'The weather is sweet', 
                 'The sun is shining and the weather is sweet, and one and one is two'])

from sklearn.feature_extraction.text import CountVectorizer 

count_vectorizer1 = CountVectorizer()  # Реализует концепцию мешка слов
vectors1 = count_vectorizer1.fit_transform(train_docs)  # Сначала запускается метод fit, а далее запускается метод transform, который return-ит вектор для каждого текста; При вызове fit получается вокабуляр слов
vectors1
