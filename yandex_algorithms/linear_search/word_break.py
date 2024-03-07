# Имеется строка s, а также список из строк. Верните True, если s можно получить из последовательного сложения элементов списка
# Input: s = "leetcode", wordDict = ["leet","code"]; Output: True


def word_break(s: str, words: str):
    idx = 0
    for word in words:
        len_of_word = len(word)
        if s[idx: idx + len_of_word] != word:
            return False
        idx += len_of_word
    return True
        

print(word_break('leetcode', ['leet', 'code']))
