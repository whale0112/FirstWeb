def solution(tile_length):
    answer = ''
    if tile_length % 6 == 0:
        answer = "RRRGGB" * (tile_length/6)
    elif tile_length % 6 == 3:
        answer = "RRRGGB" * (tile_length//6) + "RRR"
    elif tile_length % 6 == 5:
        answer = "RRRGGB" * (tile_length//6) + "RRRGG"
    else:
        answer = -1

    return answer

tile_length1 = 11
ret1 = solution(tile_length1)
print(ret1)

tile_length2 = 16
ret2 = solution(tile_length2)
print(ret2)