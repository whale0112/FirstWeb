def solution(scores):
    answer = 0
    for i in scores:
        count1 = 0
        count2 = 0
        if i[0] >= 80:
            count1 += 1
        if i[1] >= 88:
            count1 += 1
        if i[2] >= 70:
            count1 += 1

        if count1 > 1:
            if i[0] >= 40:
                count2 += 1
            if i[1] >= 44:
                count2 += 1
            if i[2] >= 35:
                count2 += 1

        print(count1, count2)
        if count2 == 3:
            answer += 1
        
    return answer

scores1 = [[30, 40, 100], [97, 88, 95]]
ret1 = solution(scores1)
print(ret1)

scores2 = [[90, 88, 70], [85, 90, 90], [100, 100, 70], [30, 90, 80], [40, 10, 20], [83, 88, 80]]
ret2 = solution(scores2)
print(ret2)