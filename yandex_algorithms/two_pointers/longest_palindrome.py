# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]

# Задача из собеса Яндекс (два указателя)


def longest_palindrome(s: str) -> str:
    res = ''
    reslen = 0
    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > reslen:
                res = s[l: r + 1]
                reslen = r - l + 1
            l -= 1
            r += 1
        
    return res


print(longest_palindrome('ttttttttttttttttttttttdtttttttttttttttttttttt'))
