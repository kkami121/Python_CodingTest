# 2차원 배열에서 인형을 뽑은 후 바구니에 넣고 같은 인형이 겹쳐서 바구니에 들어 갔을 때 인형은 사라지고 사라진 인형의 개수를 구하는 문제

def solution(board, moves):
    answer = 0
    doll_list = [] # 바구니 스택
    
    for i in moves: # 움직이는 번호에 맞는 columns
        for j in range(len(board)): # 행의 개수
            if board[j][i - 1] != 0 : # 움직이는 열에 해당하는 행을 돌리면서 값을 확인 할 때 0이 아닌 경우
                doll_list.append(board[j][i - 1]) # 그 값을 바구니 스택에 push
                board[j][i - 1] = 0 # 스택에 push한 경우 빈 값(0)으로 변경
                
                if len(doll_list) > 1: # 바구니 스택이 채워졌을 경우 부터 시작
                    if doll_list[-1] == doll_list[-2]: # 들어와 있는 값과 지금 막 들어온 값이 같은 경우 2번의 pop을 통해 인형 삭제 후 삭제된 인형 2개를 count
                        doll_list.pop() 
                        doll_list.pop()

                        answer +=2
                break    
    return answer

