N, M = map(int, input('행, 열 : ').split())

def solution(N,M):
    result = 0
    for i in range(N):
        raw = list(map(int, input('행 요소 입력 : ').split()))
        raw_pick = min(raw)
        result = max(result,raw_pick)
    return result

print(solution(N,M))