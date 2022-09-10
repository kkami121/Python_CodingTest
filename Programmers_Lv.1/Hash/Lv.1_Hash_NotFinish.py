# 해시를 이용해서 마라톤 참가자 중 완주 하지 못한 사람 찾기

def solution(participant, completion):
    hashDict = {} # 해시를 위한 dict
    sumHash = 0 # 해시로 받은 숫자 저장
    
    for part in participant:
        hashDict[hash(part)] = part # {4221083198511898609: 'leo', -327789713143004153: 'kiki', 5678897805613024907: 'eden'} 이런식으로 만들어줌
        sumHash += hash(part) # 모든 해시 값을 더해
    
    for comp in completion: 
        sumHash -= hash(comp) # 완주한 사람에 해당하는 해시값을 뺍
    
    # 4. 남은 값이 완주하지 못한 선수의 hash 값이 된다

    return hashDict[sumHash] # 남은 해시값을 가진 dict를 리턴하면 해당 사람이 남음

