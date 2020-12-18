# 팩토리얼 구현 math함수와 재귀함수, 반복문 이용
# 1. 재귀함수
def factorial_recursive(n):
    if n<= 1:
        return 1
    return n*factorial_recursive(n-1)

print(factorial_recursive(5))

# 2. 반복문 사용
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial_iterative(5))

# 3. math함수 이용
import math
print(math.factorial(5))