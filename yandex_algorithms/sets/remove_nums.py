# Удалить из последовательности наименьшее кол-во чисел, чтобы все оставшиеся отличались между собой не более
# чем на 1. В отведе выдать кол-во удалённых элементов. 
# Пример: 1 2 3 1 3 3 # Удаляем 1 1

# Идея: для решения задачи минимизации --> решаем максимизацию в цикле

def word_count_remove(nums: list[int]):
    nums.sort()
    d = {}
    for num in nums:
        d[num] = d.get(num, 0) + 1
    
    ans = 0
    for key in d:
        now = d.get(key, 0) + d.get(key + 1, 0)
        ans = max(ans, now)
    return len(nums) - ans
    

print(word_count_remove([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 100, 110]))
