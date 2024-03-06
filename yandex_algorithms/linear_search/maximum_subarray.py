# Частый вопрос из собеседований
# Дана множество чисел. Необходимо найти непрерывную подпоследовательность с максимальной суммой элементов


def maximum_subarray(elements: list[int]):
    max_sum, cur_sum = float('-inf'), 0

    for element in elements:
        cur_sum = max(cur_sum + element, element)
        max_sum = max(max_sum, cur_sum)

    return max_sum


print(maximum_subarray([1, 2, 3, -5, 4, 10, 11, 12, 13]))
