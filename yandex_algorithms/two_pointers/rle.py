# Дана строка (возможно, пустая) состоящая из букв A-Z AAAABBBCCCA
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C3A 

# Методом двух указателей

def rle(s: str) -> str:
    ans = ''
    i, j = 0, 0
    while i < len(s):
        cur_sum = 0
        while j < len(s) and s[i] == s[j]:
            cur_sum += 1 
            j += 1

        ans += s[i] + str(cur_sum)
        i = j
    return ans.replace('1', '') 


print(rle('AAAABBBNNNNIIIITTTTUUUL'))
