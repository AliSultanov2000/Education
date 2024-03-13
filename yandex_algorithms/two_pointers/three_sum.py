# Найдите уникальные тройки чисел, такие, что их сумма равно 0

# Задача из LeetCode medium

def threesum(nums: list[int]):
    hashmap = {}  # Значение: индекс
    ans = set()

    for i, num in enumerate(nums):
        hashmap[num] = i

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            desired = -nums[i] - nums[j]
            if desired in hashmap and hashmap[desired] != i and hashmap[desired] != j:
                ans.add(tuple(sorted([nums[i], nums[j], desired])))
    
    return list(ans)


print(threesum([-1, 0, 1, 2, -1, 4]))
