# Неизвестный водила совершил ДТП и скрылся с места происшествия. Полиция опрашивает свидетелей.
# Каждый из них говорит, что запомнил какие-то буквы и цифры номера. Но при этом свидетели не помнят
# порядок этих цифр и букв. Полиция хочет проверить несколько подозреваемых авто.
# Будем говорить, что номер согласуется с показаниями свидетеля, если все символы, которые назвал 
# свидетель, присутствует в этом номере (не важно, сколько раз). 

# Выпишите номера авто, которые согласуются с максимальным кол-вом свидетелй. Если таких номеров несколько, 
# то выведите их в том же порядке, в котором они были заданы на входе. 

# Будем смотреть, является ли показания свидетеля подмножеством номера подозреваемого авто.
# Если это так, увеличим счётчик сведителей для данного авто на один


m = int(input())  # Кол-во Свидетелей
wits = []  # Свидетели
for _ in range(m):
    wits.append(set(input().strip()))

n = int(input())  # Кол-во Номеров
nums = []  # Список с кортежем: (номер, кол-во свидетелей)
maxwitcnt = 0

for i in range(n):
    num = input().strip()
    numset = set(num)
    witcnt = 0
    for wit in wits: 
        if wit <= numset:  # Если всё множество numset включает в себя wit
            witcnt += 1
    nums.append((num, witcnt))
    maxwitcnt = max(maxwitcnt, witcnt)


ans = []  # Ответ с номерами, которые чаще всего встречались (их может быть несколько, если они равны)
for num in nums: 
    if num[1] == maxwitcnt:
        ans.append(num[0])
print('\n'.join(ans))  # Печатаем через пробел
