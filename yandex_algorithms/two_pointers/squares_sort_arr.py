# Дан массив с отсортированными числами (есть отриц числа), верните отсортированный массив квадратов чисел

def squares_sort(nums: list[int]) -> list[int]:
    l, r = 0, len(nums) - 1
    arr = []
    while l != r:
        if abs(nums[r]) > abs(nums[l]):
            arr.append(nums[r] ** 2)
            r -= 1
        else:
            arr.append(nums[l] ** 2)
            l += 1

    return arr[::-1]


nums = list(map(int, input().split()))
print(squares_sort(nums))
