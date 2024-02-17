# Дана последовательность чисел длиной N. 
# Необходимо найти кол-во отрезков с нулевой суммой. 

# Решение за O (N^2)

def count_zeroes_sum_o2(nums):
    cntranges = 0 
    for i in range(len(nums)): 
        rangesum = 0
        for j in range(i, len(nums)): 
            rangesum += nums[j]
            if rangesum == 0: 
                cntranges += 1
    return cntranges
