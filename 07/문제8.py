def solution(n, votes):
    A = [0] * n
    for a in range(1, n + 1, 1):
        for b in range(0, len(votes), 1):
            if votes[b] == a:
                A[a - 1] += 1
    print(A)
    for c in range(0, len(A), 1):
        print(A[c] , n/2)
        if A[c] > len(votes)/2:
            return c + 1
    return -1

n1 = 3
votes1 = [1, 2, 1, 3, 1, 2, 1]
ret1 = solution(n1, votes1)
print(ret1)

n2 = 2
votes2 = [2, 1, 2, 1, 2, 2, 1]
ret2 = solution(n2, votes2)
print(ret2)








# def solution(tv):
#     answer = 0

#     used_tv = [0] * 25

#     for a in programs:
#         for b in range(a[0], a[1], 1):
#             used_tv[b] += 1

#     print(used_tv)
#     for c in used_tv:
#         if c >= 2:
#             answer += 1

#     return answer

# programs = [[1, 6], [3, 5], [2, 8]]
# ret = solution(programs)
# print(ret)
