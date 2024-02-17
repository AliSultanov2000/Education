# Дана отсортированная последовательность чисел длиной N и число K
# Необходимо найти кол-во пар чисел A,B, таких, что B - A > K 

# Возьмём наименьшее число и найдём для него первое подходящее большее. Всё еще большие числа точно подходят.
# Возьмём в качестве меньшего числа следующее, а указатель первого подходящего большего будем двигать начиная
# c той позиции, где он находится сейчас

# Нет смысла двигать правый указатель левее

def cnt_pairs_with_diff(sortednums, k): 
    cnt_pairs = 0 
    last = 0 
    for first in range(len(sortednums)): 
        while last < len(sortednums) and sortednums[last] - sortednums[first] <= k:
            last += 1
        cnt_pairs += len(sortednums) - last
    return cnt_pairs
