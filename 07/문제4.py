def solution(classes, m):
    answer = 0
    for i in classes:
        if i % 30 == 0:
            answer += i/30
        else:
            answer += i//30 + 1
    return answer

classes = [80, 45, 33, 20]
m = 30
ret = solution(classes, m)
print(ret)