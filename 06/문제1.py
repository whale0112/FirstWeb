# score 점수를 가진 학생이 몇등인지
def func_a(scores, score):
    rank = 1
    for i in range(0, 4, 1):
        if scores[i] > score:
            rank += 1
        else: 
            return rank
    # for s in scores:
    #     if s == score:
    #         return rank
    #     else:
    #         rank += 1

    return rank

def func_b(arr): # 내림차순으로 정렬
    #정렬하는 함수
    arr.sort(reverse=True)
    print(arr)

#정렬된 점수에서 n번째 학생 찾기
def func_c(arr, n):
    return arr[n]

def solution(scores, n):
    s = func_c(scores, n)
    func_b(scores)
    answer = func_a(scores, s)
    return answer

scores = [20, 60, 98, 59]
n = 3
ret = solution(scores, n)
print(ret)
