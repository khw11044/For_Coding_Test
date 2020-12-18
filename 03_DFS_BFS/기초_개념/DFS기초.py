# 재귀함수로 구현 데이터개수가 N -> O(N)
# 인접한 노드들중 가장 작은 번호의 노드만 우선적으로 방문처리함, 깊이
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

# DFS 메서드 정의
def dfs(graph,v,visited):
    visited[v] = True
    print(v,end=' ')

    for i in graph[v]:
        if not visited[i]:      # 연결된 노드가 방문 처리 안됐으면 재귀적으로 반복, 노드 번호가 가장 낮은것이 우선적으로 
            dfs(graph,i,visited)

dfs(graph,1,visited)
