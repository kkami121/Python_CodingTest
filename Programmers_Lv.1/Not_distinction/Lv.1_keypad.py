# 키패드에서 번호를 누룰 때 가까운 손으로 누르고 누르는 손을 출력하는 문제

def solution(numbers, hand):
    answer = ''
    key_dict = { 1 : [0, 0], 2 : [0, 1], 3 : [0, 2],
                 4 : [1, 0], 5 : [1, 1], 6 : [1, 2],
                 7 : [2, 0], 8 : [2, 1], 9 : [2, 2],
               '*' : [3, 0], 0: [3, 1], '#' : [3, 2]
                }       
    
    left = [1, 4, 7]
    right = [3, 6, 9]
    lhand = '*'
    rhand = '#'
    
    for i in numbers: # 1, 4, 7 은 왼손
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right: # 3, 6, 9 오른손
            answer += 'R'
            rhand = i
        else: # 2, 5, 8, 0 은 거리를 계산해서 결정
            current_point = key_dict[i] # 찾고 싶은 값
            left_point = key_dict[lhand] # 현재 왼손의 위치
            right_point = key_dict[rhand] # 현재 오른손 위치
            left_dict = abs(current_point[0] - left_point[0]) + abs(current_point[1] - left_point[1]) # 찾고 싶은 값으로 가기 위한 왼손에서 부터 전체 거리(찾고 싶은 값의 x축 - 왼손 x축 + 찾고 싶은 y축 - 왼손 y축) 
            right_dict = abs(current_point[0] - right_point[0]) + abs(current_point[1] - right_point[1])# 찾고 싶은 값으로 가기 위한 왼손에서 부터 전체 거리(찾고 싶은 값의 x축 - 오른손 x축 + 찾고 싶은 y축 - 오른손 y축)

            if left_dict < right_dict: # 왼손 거리가 작으면 즉, 거리가 가까우면
                answer += 'L'
                lhand = i
            elif left_dict > right_dict: # 오른손 거리가 가까우면
                answer += 'R'
                rhand = i
            else: # 거리가 같은 경우 주어진 hand(왼손잡이 or 오른손잡이)에 따라 결정
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i
    return answer

