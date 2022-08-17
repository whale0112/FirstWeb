def solution(papers, K):
    length = len(papers)
    for i in range(0, length, 1):
        K -= papers[i]
        if K < 0:
            return i
    return length

papers1 = [2, 4, 2, 3, 1]
K1 = 10
ret1 = solution(papers1, K1)
print("solution 함수의 반환 값은", ret1, "입니다.")

papers2 = [2, 4, 2, 3, 1]
K2 = 14
ret2 = solution(papers2, K2)
print("solution 함수의 반환 값은", ret2, "입니다.")