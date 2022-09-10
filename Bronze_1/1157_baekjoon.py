# 백준 1157번 단어 공부
# 주어진 알파벳에서 가장 많이 사용된 알바펫을 출력
# 가장 많이 사용된 알바펫의 개수가 중복될 경우 ? 출력

word = input()
alphabet = list(set(word))

alphabet_count = []

for i in alphabet:
   alphabet_count.append(word.count(i))

if alphabet_count.count(max(alphabet_count)) > 1:
    print('?')
else:
    print(alphabet[alphabet_count.index(max(alphabet_count))])