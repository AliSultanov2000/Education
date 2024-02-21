# Вставка элемента в отсортированный массив 

mass = list(map(int, input().split()))
element = int(input())

l = 0 
r = len(mass)

while l < r: 
    m = (l + r) // 2
    if mass[m] >= element: 
        r = m
    else: 
        l = m + 1

# Нашли индекс, вставили его в массив
mass.insert(l, element)
print(mass)
