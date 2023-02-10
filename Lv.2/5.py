# 괄호 잘 닫았는지 true false

# 개수는 x (한번 나왔으면 )이게 나오는게 정상
# 간다하게 처음에 )나 마지막에 (가 나오면 false이자나 => ()) 처럼 짝이 안맞지만 처음이 )아니고 마지막이 (가 아니지만 잘못된 경우가 있음

s = '()()'

a = s.count('(')
b = s.count(')')

if s[:1] == ')' or s[-1:] == '(' or a != b:
    print(False)
else:
    print(True)



# 다른 풀이

def solution(s): # 스택사용
    OPEN = '('
    CLOSE = ')'
    count = 0

    for char in s:
        if char == OPEN:
            count += 1
        if char == CLOSE:
            count -= 1
        # count값이 0보다 작아졌다는 뜻은, 이미 짝이 맞지 않는다는 뜻이므로 early return
        # ex: '())', ')(' 이런 경우
        if count < 0:
            return False

    return count == 0



def solution(s):
    stack = []
    for i in s:
        if i == '(':  # '('는 stack에 추가
            stack.append(i)
        else:  # i == ')'인 경우
            if stack == []:  # 괄호 짝이 ')'로 시작하면 False 반환
                return False
            else:
                stack.pop()  # '('가 ')'와 짝을 이루면 stack에서 '(' 하나 제거

    return stack==[]