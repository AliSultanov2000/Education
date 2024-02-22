# Дан массив чисел (не отсортированный), и в массиве есть только один дубликат числа. Необходимо найти индекс этого дубля.

nums = list(map(int, input().split()))
check_dublicate_set = set()

for i in range(len(nums)): 
    if nums[i] in check_dublicate_set:
        print(i)
    else:
        check_dublicate_set.add(nums[i])
