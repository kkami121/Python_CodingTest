# 기본적으로 가장 큰 값과 가장 작은 값을 곱하게 해야함
# 내가한건 최솟값 최대값 곱하고 pop하는 식의 반복문 : 효율성에서 걸림
A = [1, 4, 2]
B = [5, 4, 4]
answer = 0

for i in range(len(A)):
    answer += min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))

print(answer)

# 다른 사람 풀이 : A를 최솟값(오름차순)부터 정렬 B를 최대값(내림차순)부터 정렬 후 서로 곱하고 더하기

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True) # 최대값부터 정렬 즉 내림차순
    for i in range(len(A)):
        answer += (A[i]*B[i])
    return answer


# 다른 사람 풀이 : A를 최솟값(오름차순)부터 정렬 B를 최대값(내림차순)부터 정렬 후 zip을 이용해서 (1, 5)처럼 만들고 곱하기
def solution(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))