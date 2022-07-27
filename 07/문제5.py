def solution(calorie):
    answer = 0
    min = calorie[0]
    
    for i in range(1, len(calorie), 1):
        if calorie[i] <= min:
            min = calorie[i]
        else:
            answer += calorie[i] - min

    return answer

calorie = [713, 665, 873, 500, 751]
ret = solution(calorie)
print(ret)