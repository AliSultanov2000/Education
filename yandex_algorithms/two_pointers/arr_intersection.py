# Дана строка s, верните максимальную длину последнего слова (чтобы не было в ней пропусоков)
# Input: s = 'hello world'; Output: 5 (world имеет длину 5)


def arr_intersection(arr1, arr2):
    ans = []
    preparing = []

    if len(arr2) < len(arr1):
        arr1, arr2 = arr2, arr1

    for i in arr1:
        if (i in arr2) and (i not in preparing):
            ans.append(i)
            preparing.append(i)
    
    return ans


print(arr_intersection([1, 2, 3, 5, 8], [8, 1, 1, 2, 3, 4, 0]))
