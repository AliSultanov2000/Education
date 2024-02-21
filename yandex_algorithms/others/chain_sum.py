# Напишите функцию, которая при каждом вызове будет возвращать результат суммы от предыдущего вызова

def chain_sum():
    result = 0
    def inner_func(val):
        nonlocal result
        result += val
        return result
    
    return inner_func


a = chain_sum()
print(a(5))
print(a(10))
print(a(100))
print(a(200))
