def solution(day, numbers):
    count = 0
    if day % 2 == 0:
        for a in numbers:
            if a % 2 == 0:
                count += 1
    
    else:
        for a in numbers:
            if a % 2 == 1:
                count += 1
    
    return count

day = 17
numbers = [3285, 1724, 4438, 2988, 3131, 2998]
ret = solution(day, numbers)
print(ret)