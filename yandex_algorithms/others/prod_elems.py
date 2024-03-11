# Найдите для каждого эл-та массива произведение всего массива за исключением 
# самого себя 

# Inputs: [1, 2, 3, 4]
# Output: [24, 12, 8, 6]


from functools import reduce


nums = list(map(int, input().split()))
ans = []

for idx in range(len(nums)):
    prev_arr = nums[0: idx]
    next_arr = nums[idx + 1:]
    
    curr_arr = prev_arr + next_arr
    ans.append(reduce(lambda x, y: x * y, curr_arr))

print(ans)
