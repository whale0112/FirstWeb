def solution(num_apple, num_carrot, k):
    answer = 0
    
    if num_apple < (3 * num_carrot):
        answer = num_apple // 3
    else:
        answer = num_carrot

    remain_apple = num_apple - (3 * answer)
    remain_carrot = num_carrot - answer
    print(remain_carrot, remain_apple)

    k = k - remain_apple - remain_carrot

    while k > 0:
        answer -= 1
        k -= 4

    return answer

num_apple1 = 5
num_carrot1 = 1
k1 = 2
ret1 = solution(num_apple1, num_carrot1, k1)
print(ret1)

num_apple2 = 10
num_carrot2 = 5
k2 = 4
ret2 = solution(num_apple2, num_carrot2, k2)
print(ret2)