# Предположим, что массив длиной n, отсортированный в порядке возрастания,
# поворачивается от 1 до n раз.
# Например, массив nums = [0,1,2,4,5,6,7] может стать:
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.

# Найдите минимальный элемент в массиве: задача из собеса в Facebook 

def find_min(nums: list[int]):
    l = 0
    r = len(nums) - 1
    if nums[l] <= nums[r]:  # Проверяем не пришел ли к нам на вход сортиров.масс
        return nums[0]
    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[m + 1]:
            return nums[m + 1]
        elif nums[m] > nums[r]:  # Если находимся в левой части массива
            l = m + 1
        else:
            r = m  # Если находимся в правой части массива


    
print(find_min([10, 9, 8, 7, 6]))