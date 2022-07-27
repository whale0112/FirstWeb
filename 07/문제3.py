def add_score(arr):
    answer = 0
    for i in arr:
        if i == "a":
            answer += 1
        elif i == "b":
            answer += 2
        elif i == "c":
            answer += 3
        elif i == "d":
            answer += 4
        else:
            answer += 5
    return answer

def solution(n, bundle):
    A = []
    B = []

    for i in range(0, n * 2, 1):
        if i % 2 == 0:
            A.append(bundle[i])
        else:
            B.append(bundle[i])

    A_score = add_score(A)
    B_score = add_score(B)

    if A_score > B_score:
        return [1, A_score]
    elif A_score < B_score:
        return [2, B_score]
    else:
        return [0, A_score]

n = 4
bundle = "cacdbdedccbb"
ret = solution(n, bundle)
print(ret)