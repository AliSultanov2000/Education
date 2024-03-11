# Имеется изображение с  матрицей n x n, переверните изображение по горизонтали, затем инвертируйте его и верните результирующее изображение.
# Перевернуть изображение по горизонтали означает, что каждая строка изображения перевернута.
# Например, переворачивание [1,1,0] по горизонтали приводит к [0,1,1].
# Инвертирование изображения означает, что каждый 0 заменяется на 1, а каждый 1 заменяется на 0.
# Например, инвертирование [0,1,1] приводит к [1,0,0]

# Задача на два указателя

def check_func(elem: int) -> int:
    if elem == 0:
        return 1
    return 0 


def image_flip(arr: list[int]) -> list[int]:
    for row in range(len(arr)):
        l, r = 0, len(arr[row]) - 1 
        while l <= r: 
            arr[row][l], arr[row][r] = arr[row][r], arr[row][l]
            arr[row][l], arr[row][r] = check_func(arr[row][l]), check_func(arr[row][r])
            l += 1
            r -= 1
    return arr


print(image_flip([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
