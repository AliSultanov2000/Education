# Один бизнесмен решил выгодно вложить свои средства и собрался поддержать на выборах некоторые партии
# Чтобы повлиять на исход выборов, бизнесмен собирается выделить деньги на агитационную работу среди
# жителей страны. Исследования рынка показало, что для того, чтобы один житель сменил свои полит.
# воззрения, требуется потратить одну условную единицу. Кроме того, чтобы i-я партия в случае победы 
# сформировала правительство, которое будет действовать в интересах бизнесмена, необходимо дать лидеру
# партии взятку в размере pi условных единиц. При этом некоторые партии оказались идеологически устой-
# чивыми и не согласны на сотрудничество ни за какие деньги.

# По результатам последних опросов известно, сколько граждан планируют проголосовать за каждую партию
# перед началом агитационной компании. Помогите бизнесмену выбрать, какую партию следует подкупить,
# и какое кол-во граждан придётся убедить сменить свои полит.воззрения, чтобы выбранная партия победила.
# учитывая, что бизнесмен хочет потратить на всю операцию мин кол-во денег.

# Решение: отсортируем партии по возрастанию. "подстрижем" все партии до определенного уровня.
# Необходимо найти максимально высокий уровень стрижки голосов. - бин поиск
# По известному уровню стрижки чтобы посчитать кол-во голосов, которые достались нашей партии - внутр.бин поиск


def getcntvotes(i, voters, suffixsum, level):
    """
       Внутренний бин.поиск. Сколько голосов мы получим от стрижки по level.
       Ищем первую партию, которая выше 
    """
    l = 0
    r = len(voters) - 1
    while l < r:
        m = (l + r) // 2
        if voters[m][0] < level:
            l = m + 1
        else:
            r = m
    if voters[l][0] < level:
        return 0
    cntvotes = suffixsum[l] - level * (len(voters) - l)
    if voters[i][0] >= level: 
        cntvotes -= (voters[i][0] - level)
    return cntvotes

 
def model(voters, i, suffixsum):
    """
       Определение кол-ва денег для победы i-ой партии.
       Бин поиск по уровню стрижки голосов
    """
    l = 0
    r = 10 ** 6
    while l < r:
        level = (l + r + 1) // 2  # уровень стрижки
        cntvotes = getcntvotes(i, voters, suffixsum, level)  # сколько голосов от других партий уйдет к нам
        if cntvotes > voters[i][0] > level:
            l = level
        else:
            r = level - 1
    cntvotes = getcntvotes(i, voters, suffixsum, l)  # Пересчёт голосов с учётом докиданных
    recovery = max(0, voters[i][0] + cntvotes - l - 2)  # Докидывание обратно голосов. Хотим возвышаться максимум на 2 голоса
    return cntvotes - recovery, l, recovery


# чтение данных
n = int(input())  # Кол-во партий
p = [0] * n  # Взятка правительству
voters = [0] * n  # Голоса партий
for i in range(n):
    v, p[i] = map(int, input().split())
    voters[i] = (v, i)

# сортировка по возрастанию голосов и подсчёт суффиксных сумм
voters.sort()
suffixsum = [0] * n
suffixsum[-1] = voters[-1][0]
for i in range(n - 2, -1, -1):
    suffixsum[i] = suffixsum[i + 1] + voters[i][0]  # Делаем чтобы посчитать площадь фигуры


# перебор подходящих партий
mincost = 10 ** 6 + 10 ** 6 + 1
for i in range(n):
    if p[voters[i][1]] != -1:  # Если партия идеологически неустойчивая
        cost, level, recovery = model(voters, i, suffixsum)
        if p[voters[i][1]] + cost < mincost:
            mincost = p[voters[i][1]] + cost
            ans = [i, cost, level, recovery]


# восстановление и вывод ответа
winner, cost, level, recovery = ans
resvotes = [0] * n
for i in range(n):
    if i == winner:
        resvotes[voters[i][1]] = voters[i][0] + cost
    elif voters[i][0] <= level:
        resvotes[voters[i][1]] = voters[i][0]
    else: 
        if recovery > 0: 
            resvotes[voters[i][1]] = level + 1
            recovery -= 1
        else: 
            resvotes[voters[i][1]] = level

 
print(mincost)
print(voters[winner][1] + 1)
print(*resvotes)
