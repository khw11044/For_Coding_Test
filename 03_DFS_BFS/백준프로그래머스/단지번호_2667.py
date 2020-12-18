# 묶음 문제이다 --> DFS 음료수얼려먹기 문제
# 1인것끼리 묶어서 하나의 단지를 이룬다.
# 1인것끼리 묶어서 1단지 다른 1인것까지 묶어서 2단지, 다른 1인것까지 묶어서 3단지
# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

# 총 단지 개수와 단지의 집 개수를 오름차순으로 
# 3
# 7
# 8
# 9 

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    global nums
    if graph[x][y] == 1:
        graph[x][y] = 0
        nums += 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True  
    return False

house_nums = []
nums = 0
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            house_nums.append(nums)
            nums = 0

print(len(sorted(house_nums)))

for i in sorted(house_nums):
    print(i)



