#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(time_table, n):
    answer = 0
    count = [0] * n
    b = 0
    for a in range(0, len(time_table), 1):
        count[b] += time_table[a]
        if b == n - 1:
            b = 0
        else:
            b += 1
    for c in count:
        if c > answer:
            answer = c

    return answer

time_table1 = [1, 5, 1, 9]
n1 = 3
ret1 = solution(time_table1, n1)
print("solution 함수의 반환 값은", ret1, "입니다.")

time_table2 = [4, 8, 2, 5, 4, 6, 7]
n2 = 4
ret2 = solution(time_table2, n2)
print("solution 함수의 반환 값은", ret2, "입니다.")