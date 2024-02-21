# Найти самую длинную вложенную строку без повторных символов (каждый символ используется один раз)

s = input()

max_sub_str = 0
cur_unique_str = ''

for i in range(len(s)): 
    if s[i] not in cur_unique_str: 
        cur_unique_str += s[i]
    else:
        max_sub_str = max(max_sub_str, len(cur_unique_str))
        cur_unique_str = '' + s[i]

print(max_sub_str)
