#중요도가 높은 인쇄물을 먼저 출력하는 프로그램
def solution(priorities, location):
    answer = 0
    while True:
        max_num = max(priorities) # 리스트에서 가장 큰수를 구한다.
        for i in range(len(priorities)): # 리스트를 처음부터 확인한다
            if max_num == priorities[i]: # 만약 가장 큰 수와 리스트의 요소와 일치하면
                answer += 1 # 프린트한 것으로 간주하고 answer에 1 추가 
                priorities[i] = 0 # 프린트한 요소는 0으로 표시
                max_num = max(priorities) # 가장 큰 수를 다시 구한다.
                if i == location: # 만약 location과 i가 일치하면 answer을 반환한다. 
                    return answer
 #[1, 1, 0, 1, 1, 1]
 #[1, 1, 0, 0, 1, 1]
 #[1, 1, 0, 0, 0, 1]
 #[1, 1, 0, 0, 0, 0]
 #[0, 1, 0, 0, 0, 0] 이런식으로 진행          


from collections import deque
def solution2(priorities, location):
    answer = 0
    d = deque(priorities) # 중요도 판단
    temp = deque([x for x in range(len(d))]) # 주어진 lication을 판단하기 위한 인덱스
    while d:
        p = d.popleft() #d에서 하나씩 빠지면서 1 1 9 1 1 1 1 하나씩 출력 
        if d:
            if p < max(d): # 중요도가 가장 높은 값이 아니면 
                temp.append(temp.popleft()) #인덱스 앞에 빼서 뒤에 넣기
                d.append(p) # 위에서 하나씩 뺏으니까 중요도가 높은값이 아니면 뒤에 넣기
            else:
                answer += 1
                if temp[0] == location:
                    return answer
                else:
                    temp.popleft()
                    

    return answer + 1 # 모든 중요도가 정렬되어 있을 경우 + location = 0인 경우 1을 리턴해야하기 때문에 즉 while에 안들어가는 경우를 생각해서 + 1을 해줘야함


def solution3(priorities, location):
    answer = 0
    from collections import deque

    d = deque([(v,i) for i,v in enumerate(priorities)]) # enumerate 사용하면 밑에 처럼 생성됨
                                                        # (0, 'A')
                                                        # (1, 'B')
                                                        # (2, 'C')
    
    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item) # 위에서 pop으로 빠졌고 중요도가 제일 높은 9보다 작은 경우 뒤에 넣기
        else:
            answer += 1
            print(d)
            if item[1] == location:
                break
    return answer

solution3([1, 1, 9, 1, 1, 1], 0)

def solution4(priorities, location):
    priorities = [(v, idx) for idx, v in enumerate(priorities)]
    count = 0
    while True:
        if priorities[0][0] == max(priorities)[0]:
            count += 1
            if priorities[0][1] == location:
                break
            priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))
    return count

solution4([1, 1, 9, 1, 1, 1], 0)