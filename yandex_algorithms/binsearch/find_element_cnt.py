# Задана отсортированная по неубыванию последовательность из N чисел и число x
# Необходимо определить сколько раз число X входит в последовательность. Если такого числа нет - вернуть длину массива

# Найдём одним левым бинпоиском первое число (идкс) больше либо равное Х. А вторым левым бинпоиском - число строго большее Х.
# Разность индексов и будет кол-во вхождений

def lbinsearch(l, r, check, checkparams):
    while l < r: 
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else: 
            l = m + 1
    return l


def check_is_ge(m, params): 
    seq, x = params
    return seq[m] > x



def check_is_gt(m, params):
    seq, x = params
    return seq[m] >= x


if __name__ == '__main__':
    arr = [1, 5, 10, 10, 10, 20, 26, 30]
    val = 20
    index_ge = lbinsearch(0, len(arr), check_is_ge, (arr, val))
    index_gt = lbinsearch(0, len(arr), check_is_gt, (arr, val))
    print(index_ge - index_gt)
