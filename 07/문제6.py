def solution(point):
    answer = 0
    if point > 1000:
        answer = point//100 * 100
    return answer

point = 2323
ret = solution(point)
print(ret)