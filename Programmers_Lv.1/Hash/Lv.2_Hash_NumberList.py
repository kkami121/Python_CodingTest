# 리스트의 있는 전화번호가 다른 전화번호의 접두어 인지 확인하는 문제

# 해시 사용
def solution(phone_book):
    answer = True
    
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    
   
    for phone_number in phone_book:
        jubdoo = ""
        for number in phone_number:
            jubdoo += number # 해시에 포함되어 있는지 확인 하기 위한 작업
            if jubdoo in hash_map and jubdoo != phone_number: # 1195524421을 jubdoo로 만들면 
                answer = False                                # 1, 11, 119, 1195, 11955....으로 나가는데
                                                              # 119가 되었을 때 해시에 있는지를 확인하면 첫 번째인 '119'가 있음 => 즉 접두어가 있다는 것이다.
    return answer                                             # 그리고(and) 자기 자신은 아닌 것도 포함해야함(119가 '119'일때 제외)


# for과 startswith 사용

def solution(phoneBook):    
    # 1. 비교할 A선택
    for i in range(len(phoneBook)):
        # 2. 비교할 B선택
        for j in range(i+1, len(phoneBook)):
            # 3. 서로가 서로의 접두어인지 확인한다.
            if phoneBook[i].startswith(phoneBook[j]):
                return False
            if phoneBook[j].startswith(phoneBook[i]):
                return False
    return True

# 다른 풀이 

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True