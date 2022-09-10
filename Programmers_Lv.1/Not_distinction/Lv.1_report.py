
def solution(id_list, report, k):
    answer = [0] * len(id_list) # answer을 id_list의 크기 만큼 초기화
    reports = {x : 0 for x in id_list} # {'muzi': 0, 'frodo': 0, 'apeach': 0, 'neo': 0} 같은 모양으로 초기화

    for i in set(report):
        reports[i.split()[1]] += 1
        
    for i in set(report): # set은 중복을 허용하지 않음!!!!!!!
        if reports[i.split()[1]] >= k:
            answer[id_list.index(i.split()[0])] += 1

    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2

solution(id_list, report, k)