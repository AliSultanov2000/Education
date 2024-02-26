# Сортировка пузырьком - на каждой итерации должен всплыть один пузырёк

nums = list(map(int, input().split()))

for _ in range(len(nums) - 1):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
 
print(nums)
