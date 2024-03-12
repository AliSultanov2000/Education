# Дан отсортированный массив. Найдите индексы любых элементов, которые в сумме дают target число
# Если таких нет, то верните -1

# LeetCode medium (two pointers)

def two_sum_sorted(nums: list[int], target: int):
    l, r = 0, len(nums) - 1
    while l <= r:
        cur_sum = nums[l] + nums[r]
        if cur_sum == target:
            return (l, r)
        elif cur_sum < target:
            l += 1
        else:
            r -= 1
    return -1


print(two_sum_sorted([1, 2, 3, 4, 5], 6))
