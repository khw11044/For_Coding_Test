# 연구소, 재귀함수
# 연구소에서 인체에 치명적인 바이러스 유출
# 바이러스 확산을 막기 위해서 연구소에 벽을 세움
# 연구소의 크기는 N x M 
# 바이러스는 상 하 좌 우로 인접한 빈칸으로 모두 퍼져나감
# 세울수 있는 벽의 개수는 3개 3개를 모두 사용
# 안전 영역의 개수는 ? 

# 요약 : 상하좌우로 퍼지는 바이러스 막기, 바이러스는 2, 벽은 1, 빈공간이며 안전공간은 0, 0의 개수는?

n,m = map(int, input().split())

data = []
temp = [[0]*m for _ in range(n)]                    # 벽 설치한 뒤 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))    # 초기 맵 상태

# 상하좌우 퍼짐
dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = 0

# 바이러스 퍼지기
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 바이러스가 퍼질수 있는 범위
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx,ny)

# 안전영역 몇개인지 세는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1

    return score

# dfs를 이용해서 울타리를 설치하는 모든 경우를 하면서 매번 안전 영역 개수를 계산하여 이전이랑 비교하며 최대값을 계산 
def dfs(fence):
    global result
    # 울타리가 3개 설치가 완료된경우
    if fence == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j] # 울타리가 3개 설치된 새로운 연구소 맵
        
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:   # 모든 연구소를 훑으면서 바이러스가 있는곳을 찾음
                    virus(i,j)  # 바이러스가 있는 곳을 기준으로 퍼지는 함수 발생

        result = max(result,get_score())
        return
    
    # 울타리 3개 설치하기
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1      # (i,j) 위치에 울타리 설치됨
                fence += 1          # fence 개수 3개까지 늘림
                dfs(fence)      
                data[i][j] = 0
                fence -= 1

dfs(0)
print(result)