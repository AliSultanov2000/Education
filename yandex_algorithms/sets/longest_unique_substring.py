# Дана строка, необходимо найти максимально длинную подстроку с уникальными элементами

def longest_substring(s: str) -> int:
    ans = 0

    unique_letters = set()
    cur_res = 0
    for i in s:
        if i not in unique_letters:
            unique_letters.add(i)
            cur_res += 1
        else:
            cur_res = 0
            unique_letters.clear()

        ans = max(ans, cur_res)
    return ans



print(longest_substring('sdfsdf'))
