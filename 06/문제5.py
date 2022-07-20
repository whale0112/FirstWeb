def solution(member_age, transportation):
    adult_expense = 0
    child_expense = 0

    if transportation == 'Bus':
        for a in member_age:
            if a >= 20:
                adult_expense += 40000
            else:
                child_expense += 15000

    elif transportation == 'Ship':
        for a in member_age:
            if a >= 20:
                adult_expense += 30000
            else:
                child_expense += 13000

    elif transportation == 'Airplane':
        for a in member_age:
            if a >= 20:
                adult_expense += 70000
            else:
                child_expense += 45000

    if len(member_age) >= 10:
        adult_expense = adult_expense * 90/100
        child_expense = child_expense * 80/100

    total_expense = adult_expense + child_expense

    return total_expense

member_age1 = [13, 33, 45, 11, 20]
transportation = "Bus"
ret1 = solution(member_age1, transportation)
print(ret1)

member_age2 = [25, 11, 27, 56, 7, 19, 52, 31, 77, 8]
transportation = "Ship"
ret2 = solution(member_age2, transportation)
print(ret2)

