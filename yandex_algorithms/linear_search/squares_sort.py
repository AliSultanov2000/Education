# Сгруппировать слова по общим буквам
# Пример: Input: ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
# Output: [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]


# Может быть на собеседовании

def groupwords(words):
    groups = {}
    for word in words:
        sortedword = ''.join(sorted(word))
        if sortedword not in groups:
            groups[sortedword] = []
        groups[sortedword].append(word)
    
    ans = []
    for sortedword in groups:
        ans.append(groups[sortedword])
    return ans
