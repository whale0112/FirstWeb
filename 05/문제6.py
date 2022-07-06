def solution(number):
    count = 0
    for i in range(1, number + 1):
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
            count += 1
        if i // 10 == 3 or i // 10 == 6 or i // 10 == 9:
            count += 1
        if i // 100 == 3 or i // 100 == 6 or i // 100 == 9:
            count += 1

    return count

number = 40
ret = solution(number)
print(ret)