# DFS 묶음을 찾아 묶음 개수를 알려주는 프로그램

# N x M 크기의 얼음 틀, 구멍 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시
# 구멍이 뚫려있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주
# 얼음틀 주어졌을때, 생성되는 총 아이스크림의 개수를 구하시오

# 예 : 4 x 5 크기의 얼음 틀
# 00110
# 00011
# 11111
# 00000

# --> 0끼리 붙어 있는 것이 3개, 즉 묶음을 찾아주는 프로그램이다.
# DFS로 풀기

n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input()))) # 행의 크기만큼 반복해서 행을 삽입

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:  # 범위에 벗어나면 False
        return False
    
    if graph[x][y] == 0:    # 0이 방문하지 않은 것이라고 생각하면 방문되지 않는곳을 방문한것으로 만들자
        graph[x][y] = 1     # 방문처리됨
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True         # 0이였다가 1이된 노드는 True가 됨
    
    return False            # 0이 아니라면 False

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:    # [0,0]에서 쫙 0인것들이 1이되면서 1인 노드를 만나면 멈춤 그게 한 덩어리가 됨
            result += 1

print(result)




