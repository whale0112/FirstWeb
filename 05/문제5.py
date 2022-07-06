def solution(arr):
    left = 0
    right = len(arr) - 1
    for x in range(len(arr)//2):
        temp = arr[left + x]
        arr[left + x] = arr[right - x]
        arr[right - x] = temp
    return arr

def solution2(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

arr = [1, 4, 2, 3]
ret = solution(arr)
print(ret)
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ret = solution(arr)
print(ret)