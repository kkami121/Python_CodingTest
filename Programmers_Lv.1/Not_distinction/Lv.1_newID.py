import string
import re

def solution(new_id):
    
    # 1단계
    new_id = new_id.lower() 

    # 2단계
    new_id_2 = ''
    for i in new_id: 
        if i in string.ascii_lowercase:
            new_id_2 += i
        elif i in string.digits:
            new_id_2 += i
        elif i in '-':
            new_id_2 += i
        elif i in '_':
            new_id_2 += i
        elif i in '.':
            new_id_2 += i
        else : 
            pass
    
    # 3단계
    while '..' in new_id_2:
        new_id_2 = new_id_2.replace('..', '.')
        
    # 4단계
    new_id_2 = new_id_2.strip('.')
    
    # 5단계
    if new_id_2 == '':
        new_id_2 += 'a'
    
    # 6단계
    if len(new_id_2) >= 16:
        new_id_2 = new_id_2[:15]
        new_id_2 = new_id_2.strip('.')
    
    # 7단계
    while len(new_id_2) < 3:
        new_id_2 += new_id_2[-1]
    
    answer = new_id_2
    return answer
    

