import math
from re import S

def solution(scores):
    answer = 0
    a = 0
    b = 100
    for s in scores:
        if s > a:
            a = s
        if s < b:
            b = s

    print(a, b)
    d = sum(scores) - a - b
    c = len(scores) - 2
    answer = d//c
    return answer

scores1 = [35, 28, 98, 34, 20, 50, 85, 74, 71, 7]
ret1 = solution(scores1)
print(int(ret1))

scores2 = [1, 1, 1, 1, 1]
ret2 = solution(scores2)
print(int(ret2))