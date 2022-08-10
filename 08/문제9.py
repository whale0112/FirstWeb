#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(score):
    answer = [1] * len(score)
    for a in range(0, len(score), 1):
        for b in range(0, len(score), 1):
            if score[a] < score[b]:
                answer[a] += 1
        
    return answer

score1 = [90, 87, 87, 23, 35, 28, 12, 46]
ret1 = solution(score1)
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

score2 = [10, 20, 20, 30]
ret2 = solution(score2)
print("solution 함수의 반환 값은 ", ret2, " 입니다.")





def solution(characters):
    result = ""
    result += characters[0]
    for i in range(1, len(characters), 1):
        if characters[i] != characters[i - 1]:
            result += characters[i]
    return result

characters = "senteeeencccccceeee"
ret = solution(characters)
print(ret)