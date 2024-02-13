# В отсортированном массиве найти индекс первого элемента, большего заданного числа
# Пробегаемся по индесам массива. m - индекс; 

def lbinsearch(l, r, check, checkparams):
    while l < r: 
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else: 
            l = m + 1
    return l


def check_val(m, checkparams):
    sequence, val = checkparams
    return sequence[m] > val



if __name__ == '__main__':
    arr = [1, 5, 7, 10, 14, 18]
    print(lbinsearch(0, len(arr), check_val, (arr, 1000)))
