# 스택은 선입선출 : 먼저들어온게 먼저 나간다.
from collections import deque

queue = deque()
#삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(4)-삭제()
queue.append(5)
print(queue)
queue.append(2)
print(queue)
queue.append(3)
print(queue)
queue.append(7)
print(queue)
queue.popleft()
print(queue)
queue.append(4)
print(queue)
queue.popleft()
print('들어온순서대로 출력:',queue)
queue.reverse
print('나중에 들어온 순으로 출력:',queue)



