# 만들수 없는 금액

# 동네 편의점의 주인인 동빈이는 N개의 동전을 가지고 있습니다. 이때 N개의 동전을 이용하여 만들 수 없는 
# 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하세요.

# 예를 들어, N = 5이고, 각 동전이 각각 3원, 2원, 1원, 1원, 9원짜리(화폐 단위) 동전이라고 가정합시다.
# 이때 동빈이가 만들 수 없는 양의 정수 금액 중 최솟값은 8원입니다.

# 또 다른 예시로, N=3이고, 각 동전이 각각 3원, 5원, 7원짜리(화페 단위) 동전이라고 가정합시다.
# 이때 동빈이가 만들 수 없는 양의 정수 금액 중 최솟값은 1원입니다.

N = int(input('돈 단위 개수 입력 : '))

coins = list(map(int, input('돈 단위 입력 : ').split()))

def solution(n,coins):

    coins.sort()

    target = 1

    for coin in coins:
        if coin > target:
            break
        target = target + coin
    
    return target

print(solution(N,coins))
