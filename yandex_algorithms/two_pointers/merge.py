# Даны два отсортированных массива. Необходимо объединить их с сохранением сортировки в итоговом массиве 

# Поставим два указателя на начало каждой из последовательностей. Выберем тот, который указывает на 
# меньшее число, запишем это число в результат и сдвинем указатель 

def merge(nums1, nums2): 
    merged = [0] * (len(nums1) + len(nums2))
    first1 = first2 = 0  # Два указателя
    for k in range(len(nums1) + len(nums2)):
        if first1 != len(nums1) and (first2 == len(nums2) or nums1[first1] <= nums2[first2]):
            merged[k] = nums1[first1]
            first1 += 1
        else: 
            merged[k] = nums2[first2]
            first2 += 1
    return merged


def merge_two_list(nums1: list[int], nums2: list[int]):
    """Методе двух указателей. Работает также с неотсортированным массивом."""
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



if __name__ == '__main__':
    print(merge([5, 10, 453, 423423], [1, 2, 3, 4, 6]))
    print(merge([1, 1, 1, 2], [2, 3, 3, 3]))
