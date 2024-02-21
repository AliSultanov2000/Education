# Задача на правильную скобочную последовательность

input = r'(('
brackets = r'{}[]()'
s = ''  # Здесь будут хранится только скобки из input

for i in input:
    if i in brackets:  # Убираем все символы, кроме скобок 
        s += i

while '()' in s or '[]'in s or '{}' in s:
	s = s.replace('()','').replace('[]','').replace('{}','')

if len(s) !=0:
	print('В скобках ошибка') 
else:
	print('Всё в порядке')
