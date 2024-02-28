def check_polyndrome(word: str):
    i, j = 0, len(word) - 1 
    middle = (len(word) // 2)

    while i <= middle and j >= middle:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True 


s = input()
print(check_polyndrome(s))
