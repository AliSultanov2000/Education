# Дан неотсортированный массив. Найдите максимальную длину последовательного подмассива. 

# Input: nums = [100, 4, 200, 1, 3, 2]; Output: 4
# Explanation: [1, 2, 3, 4] - longest consecutive subarray

# LeetCode Medium level (задача из собеседований)

def longest_consecutive(nums: list[int]) -> int:
    numset = set(nums)
    longest = 0
    for n in nums:
        if (n - 1) not in numset:  # Проверяем начало последовательности
            length = 0
        while (n + length) in numset:
            length += 1
        longest = max(length, longest)
    return longest


print(longest_consecutive([1, 5, 6, 100, 101, 102, 103]))
