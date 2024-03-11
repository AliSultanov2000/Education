def count_elements(s: str):
    cnt_elem = {}
    for i in range(len(s)):
        if s[i] not in cnt_elem:
            cnt_elem[s[i]] = 0
        cnt_elem[s[i]] += 1
    return cnt_elem 


def ransom_note(s1: str, s2: str) -> bool:
    count_s1, count_s2 = count_elements(s1), count_elements(s2) 
    for key in count_s1:
        if key not in count_s2:
            return False
        else:
            if count_s2[key] < count_s1[key]:
                return False
    return True

    
# print(ransom_note('aaab', 'aaabb'))
