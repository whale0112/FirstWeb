def solution(arr):
    count = 0
    for a in arr:
        if a/2 in arr:
            count += 1
        # for b in arr:
        #     if a/2 == b:
        #         count += 1
    
    return count

arr = [4, 8, 3, 6, 7]
ret = solution(arr)
print(ret)