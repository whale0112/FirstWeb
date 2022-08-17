#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(people):
    answer = [0] * 4
    for i in people:
        if i < 95:
            answer[0] += 1
        elif i < 100:
            answer[1] += 1
        elif i < 105:
            answer[2] += 1
        else:
            answer[3] += 1
            
    return answer

people = [97, 102, 93, 100, 107]
ret = solution(people)
print("solution 함수의 반환 값은 ", ret, " 입니다.")