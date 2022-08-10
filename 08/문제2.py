def solution(time_table):
    answer = 0
    first_class = 0
    last_class = 0
    for i in range(0, len(time_table), 1):
        if time_table[i] == 1:
            first_class = i
            break
    for i in range(len(time_table) - 1, -1, -1):
        if time_table[i] == 1:
            last_class = i
            break
    for i in range(first_class, last_class, 1):
        if time_table[i] == 0:
            answer += 1
    return answer

time_table = [1, 1, 0, 0, 1, 0, 1, 0, 0, 0]
ret = solution(time_table)
print("solution 함수의 반환 값은", ret, "입니다.")