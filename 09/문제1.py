def solution(temperature, A, B):
    answer = 0
    for i in range(A, B, 1):
        if temperature[i] > temperature[B] and temperature[i] > temperature[A]:
            answer += 1
    return answer

temperature = [3, 2, 1, 5, 4, 3, 3, 2]
A = 1
B = 6
ret = solution(temperature, A, B)
print("solution 함수의 반환 값은", ret, "입니다.")
