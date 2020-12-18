data = input('숫자 입력 : ')

def solution(data):
    result = int(data[0])
    for i in range(1,len(data)):
        num = int(data[i])
        if result <=1 or num <= 1:
            result = result + num
        else :
            result = result * num

    return result

print(solution(data))
