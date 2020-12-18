N,K = map(int, input('목표 숫자, 나눌숫자 : ').split())


def solution(n,k): 
    result = 0
    while True:
        target = (n // k) * k
        result += (n-target)
        n = target
        if n < k:
            break
        n = n // k
        result += 1
    result += n-1
    
    return result

print(solution(N,K))

