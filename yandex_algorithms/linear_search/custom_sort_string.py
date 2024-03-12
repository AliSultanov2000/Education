# Leetcode Medium level

# Input: order='cba', s = 'abcd'; Output: 'cbad'

def custom_sort_string(order: str, s: str) -> str:
    order_dict = {}

    letter_idx = 0
    for letter in order:
        if letter not in order_dict:
            order_dict[letter] = letter_idx
        letter_idx += 1
    
    return ''.join(sorted(s, key=lambda x: order_dict.get(x, 100)))


print(custom_sort_string('fgt', 'derftg'))
