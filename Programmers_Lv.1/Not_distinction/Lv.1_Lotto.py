#로또 번호를 통해 몇등인지 출력하는 문제

# 내풀이
def ranking(count):
    
    rang = 0
    if count == 6:
        rang = 1
    elif count == 5:
        rang = 2
    elif count == 4:
        rang = 3
    elif count == 3:
        rang = 4
    elif count == 2:
        rang = 5
    else:
        rang = 6
    return rang

def solution(lottos, win_nums):
    
    count = 0
    null_count = 0
    total_count = 0
    
    for i in lottos:
        if i == 0:
            null_count += 1
        for j in win_nums:
            if i == j:
                count += 1

    total_count = count + null_count
    
    
    
    answer = [0] * 2
    answer[0] = ranking(count + null_count)
    answer[1] = ranking(count)
    return answer


# 다른사람 풀이 
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
