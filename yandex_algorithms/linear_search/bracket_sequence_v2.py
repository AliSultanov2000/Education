# Правильная скобочная последовательность - реализация через стек LIFO

s = input()
stack = []
is_good = True

for i in s:
    if i in '({[':
        stack.append(i)
    elif i in '(}]':
        open_bracket = stack.pop()
        if open_bracket == '(' and i == ')':
            continue
        elif open_bracket == '{' and i == "}":
            continue
        elif open_bracket == '[' and i == ']':
            continue

        is_good = False
        break

print(is_good)
