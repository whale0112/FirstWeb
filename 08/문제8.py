def solution(usage):
    answer = 0
    if usage <= 20:
        answer = 430 * usage
    elif 21 <= usage <= 30:
        answer = 430 * 20 + 570 * (usage - 20)
    else:
        answer = 430 * 20 + 570 * 10 + 840 * (usage - 30)
    return answer

usage = 35
ret = solution(usage)
print("solution 함수의 반환 값은", ret, "입니다.")