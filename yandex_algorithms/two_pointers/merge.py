# Даны два отсортированных массива. Необходимо объединить их с сохранением сортировки в итоговом массиве 

# Поставим два указателя на начало каждой из последовательностей. Выберем тот, который указывает на 
# меньшее число, запишем это число в результат и сдвинем указатель 

def merge(nums1, nums2): 
    merged = [0] * (len(nums1) + len(nums2))
    first1 = first2 = 0 
    for k in range(len(nums1) + len(nums2)):
        if first1 != len(nums1) and (first2 == len(nums2) or nums1[first1] <= nums2[first2]):
            merged[k] = nums1[first1]
            first1 += 1
        else: 
            merged[k] = nums2[first2]
            first2 += 1
    return merged



if __name__ == '__main__':
    print(merge([5, 10, 453, 423423], [1, 2, 3, 4, 6]))
    print(merge([1, 1, 1, 2], [2, 3, 3, 3]))
