def solution(a, b):
    if a == b:
        return a
    for c in range(1, a * b + 1, 1):
        if c % a == 0 and c % b == 0:
            return c

a = 4
b = 6
ret = solution(a, b)
print("solution 함수의 반환 값은", ret, "입니다.")