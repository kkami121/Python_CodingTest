# progresses, speeds를 큐로보고 원하는 조건에 만족하면 앞에서 부터 pop
# day를 통해 하루하루 +1을 하고 speeds와 곱해서 progresses의 값을 100으로 만들기
# 100되서 pop되면 count를 +1 count가 세어지면 answer에 담고 다시 초기화
# 마지막 append(count)는 while문이 끝나면서 count가 들어있는 if을 못들어가기 때문에, 즉 마지막 count를 넣어주기

def solution(progresses, speeds):
    answer = []
    day = 0
    count = 0

    while progresses:
        if (progresses[0] + day * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            day += 1
    answer.append(count)
    return answer