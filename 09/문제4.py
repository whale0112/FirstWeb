#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(cards):
    answer = int(cards[0][1]) + int(cards[1][1]) + int(cards[2][1])

    if cards[0][0] == cards[1][0] == cards[2][0]:
        answer = (answer) * 3
    elif cards[0][0] != cards[1][0] and cards[1][0] != cards[2][0] and cards[0][0] != cards[2][0]:
        answer = answer
    else:
        answer = (answer) * 2
        

    return answer

cards1 = [["blue", "2"], ["red", "5"], ["black", "3"]]
ret1 = solution(cards1)
print("solution 함수의 반환 값은", ret1, "입니다.")

cards2 = [["blue", "2"], ["blue", "5"], ["black", "3"]]
ret2 = solution(cards2)
print("solution 함수의 반환 값은", ret2, "입니다.")
