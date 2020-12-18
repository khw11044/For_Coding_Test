# BFS, 특정 위치에서 특정위치로 이어진 노드(같은번호노드)의 최소루트거리를 알려주는 프로그램

# N x M 크기의 직사각형 형태의 미로, 미로에는 괴물이 존재, 괴물피해서 탈출
# 참여자의 현재위치는 (1,1), 미로의 출구는 (N,M)위치
# 괴물이 있는 부분, 막혀있는 부분은 0, 없는 부분은 1로 표시
# 탈출하기 위해 움직여야 하는 최소 칸의 개수, 칸을 셀때, 시작칸과 마지막 칸을 모두 포함해서 계산한다.

# 현재 노드에 가까운 노드부터 탐색하며 1인곳을 찾아가면서 이동해야 한다.

from collections import deque

n,m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의 상하 좌우
dx = [-1,1,0,0] # 상 하
dy = [0,0,-1,1] # 좌 우

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 0인곳 (괴물, 막힘)도 무시
            if graph[nx][ny] == 0:
                continue
            # 1인곳(길인곳)이 이전 노드값에 1을 더해줌, 마지막 곳은 그 길이가 나옴
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1     # 다음 노드는 = 이전 노드값 + 1
                queue.append((nx,ny))   # 큐에 다음 노드 넣기

    return graph[n-1][m-1]

print(bfs(0,0)) # 0,0부터 시작