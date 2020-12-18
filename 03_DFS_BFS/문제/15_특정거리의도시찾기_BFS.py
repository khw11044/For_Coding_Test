# 그래프에서 모든 간선의 비용이 동일할 때는 BFS(너비우선탐색)을 이용하여 최단 거리를 찾을수 있다.
# 조건 : "모든 도로의 거리는 1"
# 총 도시개수 n, 총 도로 개수 m, 출발도시는 x, 거리가 k인 도시의 개수구하기

# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4

from collections import deque

n,m,k,x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    nod, tonod = map(int, input().split())
    graph[nod].append(tonod)
    #graph[tonod].append(nod) # 양방향이동이 가능할때
    

distance = [-1]*(n+1) # 각 노드별 거리를 저장할 테이블
distance[x] = 0         # x번 노드에서 시작 

# BFS 수행
q = deque([x])

while q:
    now = q.popleft()
    # 현재 nod에서 이동할수 있는 모든 도시 확인
    for next_node in graph[now]:
        if distance[next_node] == -1:       #  방문 여부 확인
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)        # 노드(도시) 번호
        check = True

# 만약 최단 거리가 K인 도시가 없다면 -1출력
if check == False:
    print(-1)


