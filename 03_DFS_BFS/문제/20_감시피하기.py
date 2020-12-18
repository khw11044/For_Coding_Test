from itertools import combinations

n = int(input())    # 행렬 크기 n x n
board = []          # 복도 정보(n x n)
teachers = []       # 모든 선생님 위치 정보, T로 표시
spaces = []         # 모든 빈 공간 위치 정보(선생님도, 학생도 아닌 위치), X로 표시

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':  
            teachers.append((i,j))  # 선생님 위치 저장
        
        if board[i][j] == 'X':
            spaces.append((i,j))    # 장애물 설치할 수 있는(빈공간) 위치 저장

# 선생님 시력 좋아 상하좌우 끝까지 다봄 (학생발견 : True, 학생 미발견 : False)
def watch(x,y,direction):   # x,y는 선생님 위치, direction은 0,1,2,3 상하좌우  
    # 왼쪽감시
    if direction == 0:        
        while y >= 0:
            if board[x][y] == 'S':  # 학생 발견
                return True
            if board[x][y] == 'O':   # 장애물 발견
                return False
            y -= 1  # y<0이 될때까지 왼쪽을 쭈욱 감시

    # 오른쪽 감시    
    if direction == 1:  
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1

    # 위쪽 감시
    if direction == 2:  
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1

    # 아래쪽 감시
    if direction == 3:  
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1
    return False

# 장애물 설치 이후, 한명이라도 학생이 감지되는지 검사
def process():
    for x,y in teachers:    # 모든 선생님 위치 확인
        for i in range(4):  # 사방으로 확인
            if watch(x,y,i):# 학생이 발견되면 True    
                return True
    return False

find = False    # 학생이 한 명도 감지되지 않도록 설치할 수 있는지 여부

# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces,3):
    for x,y in data:
        board[x][y] = 'O'  # 장애물(O) 설치
    if not process():       # False가 리턴되었다면 --> 학생이 어느곳도 발견 안됌
        find = True
        break
    # process()가 True를 리턴했다면
    for x,y in data:
        board[x][y] = 'X'   # 설치된 장애물 없애기

for i in range(n):
    print(board[i])

if find:
    print('YES')
else:
    print('NO')