N,M,K = map(int, input('배열 수, 숫자가 더해지는 횟수, 덧셈이 연속가능한 수: ').split())

data = list(map(int, input('데이터 : ').split()))

def solution(N,M,K,data):
    result = 0
    data.sort(reverse=True)
    first_num = data[0]
    second_num = data[1]
    count = M // (K+1)
    result = (first_num*K+second_num)*count + (M-(K+1)*count)*first_num
    return result

print(solution(N,M,K,data))


