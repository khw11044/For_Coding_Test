n = int(input('모험가 수 : '))
data = list(map(int, input('각 모험가의 공포도 : ').split()))

def solution(n,data):
    data.sort()
    human_num = 0 # human number in group
    group_num = 0

    for rate in data: # 공포도
        human_num += 1
        if human_num >= rate:
            group_num += 1
            human_num = 0
    return group_num

print(solution(n,data))


