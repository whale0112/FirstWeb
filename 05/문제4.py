def func_a(arr):
    counter = [0] * 1000
    for x in arr:
        counter[x] += 1
    return counter

def func_b(counter):
    ret = 0
    for x in counter:
        if ret < x:
            ret = x
    return ret

def func_c(counter):
    ret = 1001
    for x in counter:
        if ret > x and x != 0:
            ret = x
    return ret

def solution(arr):
    counter = func_a(arr)
    max_cnt = func_b(counter)
    min_cnt = func_c(counter)
    return max_cnt // min_cnt

arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
ret = solution(arr)
print(ret)
arr = [1, 2, 3, 3, 1, 7, 8, 6, 2, 5, 6, 8, 5, 7, 4, 7, 3, 7, 9, 7, 3]
ret = solution(arr)
print(ret)