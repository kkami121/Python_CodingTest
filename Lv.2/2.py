s = '3people unFollowed me'

s = s.split(' ') # 구분점을 통해 문자열을 리스트로 만드는 방법
    
for i in range(len(s)):
    s[i] = s[i][:1].upper() + s[i][1:].lower()

print(' '.join(s))