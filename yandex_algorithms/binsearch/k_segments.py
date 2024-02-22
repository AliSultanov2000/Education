# Даны n точек на прямой, нужно покрыть их k отрезками одинаковой длины l (точки не упорядочены)
# Найдите минимальное l 

# Решение: бинарный поиск по ответу (длина отрезка)
# Будем по заданному l искать, сколько таких l необходимо, чтобы покрыть все точки на прямой
# Дальше смотрим, если нам потребовалось слишком много отрезков больше чем k, будем увеличивать l
# Иначе - будем уменьшать l


n, k = map(int, input().split())
x = list(map(int, input().split()))
x.sort()

def check_count_k(x, l):
    cnt = 0  # Кол-во необходимых отрезков для покрытия массива отрезком длиной l
    maxright = x[0] - 1
    for nowx in x:
        if nowx > maxright:
            cnt += 1
            maxright = nowx + l
    return cnt

# Минимальная, максимальная длина отрезка
left = 0  
right = x[-1] - x[0]
while left < right:
    l = (right + left) // 2
    if check_count_k(x, l) <= k:
        right = l 
    else: 
        left = l + 1

print(left)
