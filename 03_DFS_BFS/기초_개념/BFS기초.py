# BFS는 큐 자료구조에 기초한다.
# O(N) 시간이 소요, 실제 수행시간은 DFS보다 좋은편이다.
# 우선적으로 인접한 노드는 모두 방문처리를 해버림, 넓게
from collections import deque

graph = [
    [],             # 0번 노드는 없다
    [2,3,8],        # 1번 노드는 2번,3번,8번과 연결되어있다.
    [1,7],          # 2번 노드
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
n=8                 # n은 노드 개수 --> len(graph)-1
# 각 노드가 방문된 정보를 리스트 자요형으로 표현
visited = [False] * (n+1)

# BFS 메서드 정의
def bfs(graph,start,visited):
    queue = deque([start])          # deque([1])
    visited[start] = True           #현재 방문한 노드 방문처리

    while queue:                    # 큐가 빌 때까지 반복
        v = queue.popleft()         # 큐에 넣어져 있는 노드 하나를 꺼내서
        print(v, end=' ')           # 출력
        for i in graph[v]:          # 그 노드와 연결된 노드들 중
            if not visited[i]:      # 방문처리가 안되어 있다면
                queue.append(i)     # 큐에 넣는다.
                visited[i] = True   # 넣은 노드는 방문처리를 한다.

bfs(graph,1,visited)


