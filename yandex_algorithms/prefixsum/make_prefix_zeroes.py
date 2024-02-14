# Дана последовательность чисел длиной N и M запросов

# Запросы: сколько нулей на полуинтервале [l, r)


def make_prefix_zeroes(nums):
    prefixzeroes = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        if nums[i - 1] == 0:
            prefixzeroes[i] = prefixzeroes[i - 1] + 1
        else: 
            prefixzeroes[i] = prefixzeroes[i - 1]
    
    return prefixzeroes


def count_zeroes(prefixzeroes, l, r): 
    return prefixzeroes[r] - prefixzeroes[l]


if __name__ == '__main__':
    pref_zer_arr = make_prefix_zeroes([1, 5, 2, 0, 0, 1, 3, 0, 0, 5])
    print(count_zeroes(pref_zer_arr, 0, 4))
