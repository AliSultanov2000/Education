# Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую строку. Слова должны быть 
# отсортированы по убыванию их количества появления в тексте, а при одинаковой частоте появления
# - в лексикографическом порядке.  

wordcnt = {}
with open('imput.txt', 'r', encoding='utf8') as fin:
    for line in fin:
        words = line.split()
        for word in words:
            wordcnt[word] = wordcnt.get(word, 0) + 1  # Можно сделать через три строки (путём if-a)

ans = []
for word in wordcnt:
    ans.append((wordcnt[word], word))  # Располагаем в таком порядке - для удобства сортировки
ans.sort(reverse=True)

for _, word in ans: 
    print(word)
