# Сортировка слиянием использует рекурсию и алгоритм слияния двух отсортированных массивов
# Условие выхода из рекурсии - длина списка = 1


def merge_two_list(nums1: list[int], nums2: list[int]):
    """Методе двух указателей"""
    sorted_arr = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            sorted_arr.append(nums1[i])
            i += 1
        else: 
            sorted_arr.append(nums2[j])
            j += 1
    if i < len(nums1):
        sorted_arr += nums1[i:]
    elif j < len(nums2):
        sorted_arr += nums2[j:]
    return sorted_arr


def merge_sort(arr: list[int]):
    """Рекурсивная сортировка"""
    if len(arr) == 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge_two_list(left, right)


mass = list(map(int, input().split()))
print(*merge_sort(mass))
