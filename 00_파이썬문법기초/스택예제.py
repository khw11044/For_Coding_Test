# 스택은 선입후출 : 먼저들어온게 나중에 나간다.
stack = []
# pop(default=-1) pop() 파라메타는 몇번째 요소를 삭제할것인가
stack.append(5)
print(stack,'5 삽입')
stack.append(2)
print(stack,'2 삽입')
stack.append(3)
print(stack,'3 삽입')
stack.append(6)
print(stack,'6 삽입')
stack.append(7)
print(stack,'7 삽입')
print(stack[::-1],'최상단원소부터 출력') #************************************
stack.pop(3)
print(stack,'세번째 항목 삭제(pop(3))')
stack.pop()
print(stack,'마지막 항목 삭제(pop())')
stack.pop(0)
print(stack,'첫번째 항목 삭제(pop(0))')
stack.pop(1)
print(stack,'두번째 항목 삭제(pop(1))')
