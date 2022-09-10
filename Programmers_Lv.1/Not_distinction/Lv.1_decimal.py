# 리스트 중 3개 수를 더하는 조합 중 소수를 count
# 완전탐색
def solution(nums): 
    
    cnt = 0
    total = []
    
    for i in range(len(nums)): # 0번 인덱스 일 때
        for j in range(i + 1, len(nums)): # 1번 인덱스 일 떼 // 2번 // 3번
            for k in range(j + 1, len(nums)): # 2번 인덱스 / 3번 / 4번 // 3번 // 4번 /// 4번
                total.append(nums[i] + nums[j] + nums[k])
    
    
    for i in total: # 소수 : 1과 자기 자신으로나 나누어지는 수 
        idx = 0
        for j in range(1, i + 1): # 1부터 자기 자신까지 1을 더하면서 
            if i % j == 0: # 자기 자신과 1~ 자기자신 까지 나눠서 떨어지면 count
                idx += 1
        if idx == 2: # 나누어 떨어진 수 중 1과 자기자신 즉 count가 2인 i가 존재하면 count
            cnt += 1
    return cnt