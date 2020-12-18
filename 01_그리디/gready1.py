money = int(input('거슬러줘야할 돈 :'))

coins = [500,100,50,10]

def solution(money,coins):
    counts = 0
    for coin in coins:
        counts = counts + money // coin 
        money = money % coin
    
    return counts

print(solution(money,coins))
