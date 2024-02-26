# Дано N упорядоченных по неубыванию последовательностей целых чисел, в каждой из последовательностей
# ровно L элементов. Для каждых двух последовательностей выполняют следующую операцию: объединяют
# их элементы, упорядочивают их не неубыванию и смотрят, какой элемент в этой последовательности из 2L 
# элементов окажется на месте номера L (левой медианы). 
# Напишите программу, которая для каждой пары последовательности выведет левую медиану их объединения


def gensequence(l, x1, d1, a, c, m):
    """"Функция для генерации последовательностей (по условию дана)"""
    seq = [x1]
    d = d1
    for _ in range(l - 1):
        seq.append(l - 1)
        d = ((a * d + c) % m )
    return seq


def lbinsearch(l, r, check, checkparams):
    """
    Бин поиск для внутренненго нахождения кол-ва
    элементов меньших или больших текущего
    """
    while l < r: 
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l


def checkisge(index, params):
    """Условие >= x"""
    seq, x = params
    return seq[index] >= x


def checkisgt(index, params):
    """Условие > x"""
    seq, x = params
    return seq[index] > x


def cntless(seq, x):
    """Внутренний бин.поиск для нахождения кол-ва элементов < текущего"""
    ans = lbinsearch(0, len(seq) - 1, checkisge, (seq, x))
    if seq[ans] < x:
        return len(seq)
    return ans


def cntgt(seq, x):
    """Внутренний бин.поиск для нахождения кол-ва элементов > текущего"""
    return len(seq) - cntless(seq, x + 1)


def medianmerge(seq1, seq2):
    """Бинарный поиск по ответу"""
    l = min(seq1[0], seq2[0])
    r = max(seq1[-1], seq2[-1])
    while l < r: 
        m = (l + r) // 2
        less = cntless(seq1, m) + cntless(seq2, m)  # Внутренний бин.поиск для поиска кол-ва элементов < m
        gt = cntgt(seq1, m) + cntgt(seq2, m)        # Внутренний бин.поиск для поиска кол-ва элементов > m
        if less <= len(seq1) - 1 and gt <= len(seq1):
            return m
        elif gt > len(seq1):
            l = m + 1
        elif less > len(seq1) - 1:
            r = m - 1
    return l 

# Генерация последовательностей
n, l = map(int, input().split())
seqs = []
for i in range(n):
    x1, d1, a, c, m = map(int, input().split())
    seqs.append(gensequence(l, x1, d1, a, c, m))


# Проходимся по последовательностям, вызываем поиск медианы
for i in range(n):
    for j in range(i + 1, n):
        print(medianmerge(seqs[i], seqs[j]))
