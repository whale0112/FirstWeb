def solution(socks):
    answer = 0
    a = [0] * 9
    for sock in socks:
        a[sock - 1] += 1
    for b in range(0, 9, 1):
        a[b] = a[b] // 2
    for c in a:
        answer += c
        
    return answer

socks = [1, 2, 1, 3, 2, 1]
ret = solution(socks)
print("solution 함수의 반환 값은", ret, "입니다.")