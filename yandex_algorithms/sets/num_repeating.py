# Требуется проверить, повторялось ли какое-либо число в последовательности, причём расстояние между
# повторами не превосходило число k
# Если всё ок - вернуть YES; Иначе - NO

def sol(nums, k):
    lastk = set()
    for i in range(len(nums)):
        if nums[i] in lastk:
            return True
        lastk.add(nums[i])
        if i >= k:
            lastk.remove(nums[i - k])
    return False

k = int(input())
nums = list(map(int, input().split()))

if sol(nums, k):
    print('yes')
else:
    print('no')
