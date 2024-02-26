# В классе учитель хочет отправить детей на субботник таскать брёвна;
# N - кол-во чел. в классе; r - кол-во необходимых бригад; c - кол-во людей в одной бригаде
# Неудобство = разность между ростом самого высокого и самого низкого чела в бригаде;
# Помогите учителю сформировать бригады так, чтобы максимальное неудобство --> min, при этом сформировалось
# необходимое число бригад



def check(m, checkparams):
    minbrigades, c, heights = checkparams
    i = 0
    brigades = 0
    while i < len(heights) - c + 1:
        if heights[i + c - 1] - heights[i] <= m:
            brigades += 1
            i += c
        else:
            i += 1
    return brigades >= minbrigades


def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l


n, r, c = map(int, input().split())  
heights = list(map(int, input().split()))
heights.sort()

print(lbinsearch(0, heights[-1] - heights[0], check, (r, c, heights)))
