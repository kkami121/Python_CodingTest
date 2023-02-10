# 문자열을 숫자로 만들기
# list_n = list(map(int, s.split(' ')))
# s = '1 2 3 4'
def solution(s):
    list_n = list(map(int, s.split(' ')))
    return str(min(list_n)) + ' ' + str(max(list_n))