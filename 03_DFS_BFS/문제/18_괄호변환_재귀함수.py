# '(' 와 ')' 짝이 맞는지 확인 맞는곳까지 인덱스 반환 --> 이런 문자열을 균형잡힌 문자열이라고 부른다
def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1

        if count == 0:
            return i

# 균형잡힌 문자열이 옳은 문자열인지 확인
def check_proper(p):
    count = 0
    for i in p:
        if i == "(":
            count += 1
        else:
            if count == 0:  # 처음부터 ')'이면 False
                return False
            count -= 1
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]

    if check_proper(u):
        answer = u + solution(v)
    
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        
        answer += "".join(u)
    
    return answer

p = '()))((()'
print(solution(p))