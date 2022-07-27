def solution(schedule):
    answer = []
    for i in range(0, 10, 1):
        if schedule[i] == "X":
            answer.append(i + 1)
    return answer

schedule = ["O", "X", "X", "O", "O", "O", "X", "O", "X", "X"]
print(solution(schedule))