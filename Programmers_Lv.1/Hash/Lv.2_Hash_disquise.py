def solution(clothes):
    answer1 = 1
    answer2 = 0

    x = [i[0] for i in clothes]
    y = [i[1] for i in clothes]
    reports = {a : 0 for a in y}

    for i in clothes:
        reports[i[1]] += 1

    for i in reports.keys(): 
        answer1 *= reports.get(i)

    if len(reports) == 1:
        answer2 += len(clothes)
    else:
        answer2 += answer1
        answer2 += len(clothes)
        
    return answer2