def solution(words, word):
    count = 0
    for a in range(0, len(words), 1):
        for b in range(0, len(word), 1):
            if words[a][b] != word[b]:
                count += 1
    return count

words = ["CODE", "COED", "CDEO"]
word = "CODE"
ret = solution(words, word)
print(ret)