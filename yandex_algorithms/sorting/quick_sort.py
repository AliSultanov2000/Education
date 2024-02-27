def quick_sort(nums: list[int]):
    if len(nums) <= 1:
        return nums

    element = nums[0]
    left = list(filter(lambda x: x < element, nums))
    center = list(filter(lambda x: x == element, nums))
    right = list(filter(lambda x: x > element, nums))

    return quick_sort(left) + center + quick_sort(right)

mass = list(map(int, input().split()))
quick_sort(mass)
