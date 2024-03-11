# Удалить все премыкающие буквы в строке
# Input: s = 'abbaca'; Output: ca

# Задача на стэк (из собеседования Yandex)


def remove_all_adjacent(s: str) -> str:
    stack = []
    for i in s:
        if i not in stack:
            stack.append(i)
        else: 
            stack_elem = stack[-1]
            if stack_elem == i:
                stack.pop()
    return ''.join(stack)


print(remove_all_adjacent('xyz'))
