# Напишите функцию, которая проверяет, является ли число степенем четвёрки

def is_power_of_four(val: int) -> bool:
    if val < 1:
        return False
    elif val == 1:
        return True
    return is_power_of_four(val / 4)


print(is_power_of_four(256))
