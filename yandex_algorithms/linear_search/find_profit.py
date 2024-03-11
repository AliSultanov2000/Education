# Вам предоставляется массив цен, где prices[i] - это цена данной акции на i-й день.
# Вы хотите максимизировать свою прибыль, выбрав один день для покупки одной акции
# и выбрав другой день в будущем для продажи этой акции.
# Верните максимальную прибыль, которую вы можете получить от этой транзакции.
# Если вы не можете получить никакой прибыли, верните 0.

# Input: prices = [7,1,5,3,6,4]
# Output: 5 (купили в первый день, продали в 4 - й день)

prices = list(map(int, input().split()))


min_price = float('inf')    # Минимальная цена акции 
max_profit = -float('inf')  # Максимальная прибыль с продажи 

for price in prices:
    min_price = min(min_price, price)
    curr_diff = price - min_price
    max_profit = max(max_profit, curr_diff)

print(max_profit) 