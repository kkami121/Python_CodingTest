# 스택 문제
# 입력받은 숫자 리스트에서 연속으로 중복되는 값을 제거하여 새로운 리스트 만들기

# Lv.1_dollPick이랑 비슷한 문제임

def solution(arr):
    answer = []
    for i in arr:
        answer.append(i)
        if len(answer) > 1:
            if answer[-1] == answer[-2]:
                answer.pop()
    return answer