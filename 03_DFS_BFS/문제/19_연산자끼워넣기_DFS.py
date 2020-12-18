# dfs로 풀기
# 입력예시
# 3         -> 연산할 숫자 개수
# 3 4 5       -> 3개의 연산할 숫자
# 1 0 1 0   -> +,-,x,%    사칙연산중에 가능한것은 + 1개, x 1개
# --> 3+4x5 = 35 (최대값)    -> 사칙연산우선순위는 없음 무조건 왼쪽부터 연산
# --> 3x4+5 = 17 (최솟값)


n = int(input())
data = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

# 최대값, 최솟값을 초기화해주어야한다.
min_value = 1e9
max_value = -1e9

def dfs(i,now):     # i는 1~n 입력한 숫자의 순서 3:1, 4:2, 5:3, now는 현재 숫자
    global min_value, max_value, add, sub, mul, div

    if i == n:      # data 숫자만큼 수행했다면 
        min_value = min(min_value,now)
        max_value = max(max_value,now)
    
    else:
        if add > 0:
            add -= 1
            dfs(i+1,now+data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1,now-data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now*data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now / data[i]))
            div += 1

dfs(1, data[0])

print(max_value)
print(min_value)




