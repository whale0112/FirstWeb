def solution(mid_scores, final_scores):
    a = []
    b = []

    for i in range(0, len(mid_scores), 1):
        a.append(final_scores[i] - mid_scores[i])

    max = a[0]
    min = a[0]

    for i in a:
        if i > max:
            max = i
        if i < min:
            min = i
        
    return [max, min]
        
mid_scores = [20, 50, 40]
final_scores = [10, 50, 70]
ret = solution(mid_scores, final_scores)
print(ret)