# 경쟁적 전염, BFS
# n x n 크기 실험관, k는 바이러스 종류 개수, 
# 시험관 크기와 위치
# 마지막 줄은 s초 뒤에, x,y 위치

# 실험관에 s초 뒤 x,y 위치에 바이러스 종류는? 바이러스 넘버가 작은거부터 퍼짐

# 큐에 원소를 삽입할 때 낮은 바이러스의 번호부터 삽입

from collections import deque

n,k = map(int, input().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0 :  # 해당 위치에 바이러스가 존재하는 경우, 0 이아닌 바이러스 넘버  
            data.append((graph[i][j], 0, i, j)) # 바이러스 종류, 시간, 위치(i,j) 삽입

# 정렬이후 큐에 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()     # 바이러스 넘버가 낮은것부터 정렬됨
q = deque(data)

target_s, target_x, target_y = map(int,input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 너비 우선 탐색 BFS
while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break # 목표 시간이면 끝

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus # 바이러스 종류 퍼짐
                q.append((virus, s+1,nx,ny))

                for i in range(n):
                    print(graph[i])
    
    print()

print(graph[target_x-1][target_y-1])

