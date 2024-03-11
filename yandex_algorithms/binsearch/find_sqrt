# Напишите функцию, которая находит целую часть корня числа (операция возведения в степень запрещена).
# Бинарный поиск по ответу

def my_sqrt(n: int) -> int:
    l, r = 0, n

    while l < r:
        m = (l + r) // 2
        if m * m == n:
            return m
        elif m * m > n:
            r = m
        else:
            l = m + 1
    return l


print(my_sqrt(100))
