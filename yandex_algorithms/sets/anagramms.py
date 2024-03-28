# Проверить, является ли одна строка анаграммой другой 

# Анаграмма - это строка, состоящая из тех же самых букв в том же самом количестве


def make_dict(word: str):
    d = {}
    for letter in word:
        d[letter] = d.get(letter, 0) + 1
    return d


def is_anagramm(a: str, b: str):
    d1, d2 = make_dict(a), make_dict(b)
    
    for letter in d1:
        if letter not in d2 or d1[letter] != d2[letter]:
            return False
    return True


print(is_anagramm('www', 'www'))
