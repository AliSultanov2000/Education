# Дан отсортированный массив. Необходимо вернуть list с элементами без разрывов в массиве
#  Input: nums = [0, 1, 2, 4, 5, 7]; Output: ['0->2', '4->5', '7']


def summary_ranges(nums: list[int]) -> list[int]:
    s = nums[0]
    nums.append(float('inf'))
    ans = []
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] > 1:
            e = nums[i - 1]
            if s == e:
                ans.append(str(s))
            else:
                ans.append(f'{s}->{e}')
            
            s = nums[i]
    return ans
