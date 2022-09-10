# 0~9까지 숫자 중 주어진 number에 없는 숫자를 더하여 리턴하는 문제

def solution(numbers):
    answer = 0
    
    for i in range(10):
        if i not in numbers:
            answer += i
    
    return answer

