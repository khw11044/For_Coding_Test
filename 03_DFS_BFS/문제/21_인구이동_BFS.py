# 이웃한 국가의 인구수 차이가 L 이상 R이하면 국경이 열리고 인구가 섞인다. 이때 국경을 연 국가들은 연합국이된다.
# 이후 '전체 인구수' 나누기 '연합한 국가수'를 해서 인구를 분배한다.
# 몇번 국경을 개방한 횟수를 구하시오.

# BFS로 구한다. --> 인구수 차이가 조건에 맞으면 퍼져나감 단지 번호 정해주기랑 비슷

# 2 20 50
# 50 30
# 20 40

from collections import deque

# 땅크기(N), 인구 차 최소값:L, 최대값:R 입력받기
n, l, r = map(int, input().split())

# 전체 나라 인구 정보(N x N)
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

result = 0
# 특정 국가에서 출발하여 연합을 체크한 뒤에 데이터 갱신
def process(x,y,index):
    # (x,y)위치 국가와 연결된 국가(연합)의 정보를 담는 리스트
    united = []
    united.append((x,y))    # 현재국가(x,y)는 연합(united)리스트에 속함
    # 너비 우선 탐색(BFS)을 위한 큐 자료구조 정의
    q = deque()
    q.append((x,y))         # 현재 살펴보고있는 국가를 넣음
    union[x][y] = index     # 현재 연합의 번호 할당
    summary = graph[x][y]   # 현재 연합의 전체 인구수
    count = 1               # 현재 연합한 국가 수
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx,ny))           # 상하좌우 살펴 연합이 가능한 국가를 큐(q)에 넣는다.
                    union[nx][ny] = index       # 연합 국가 인증 번호를 부여받음
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx,ny))
                    for i in range(n):
                        print(union[i])
                    print()
    # 연합국가끼리 인구를 분배
    for i, j in united:
        graph[i][j] = summary // count
    for k in range(n):
        print(graph[k])
    print()
    return count

total_count = 0

# 더이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1]*n for _ in range(n)]  # 나라 처리 테이블 n x n
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:   # 해당 나라가 아직 처리되지 않았다면
                process(i,j,index)
                index += 1
    
    if index == n * n:
        break

    total_count += 1

# 인구 이동 횟수 출력
print(total_count)



