# Массив префиксных сумм должен быть на один больше 
# Массив можно построить за O(N)

# Посчитать сумму элементов массива на промежутке [l, r)

def prefixsum(arr, l, r):
    prefix_arr = [0] * (len(arr) + 1)

    for idx in range(1, len(arr) + 1):
        prefix_arr[idx] = prefix_arr[idx - 1] + arr[idx - 1]
    
    return prefix_arr


def rsq(prefixsum, l , r):
    return prefixsum[r] - prefixsum[l]
