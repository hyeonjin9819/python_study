from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for permut in permutations(dungeons, len(dungeons)):
        cnt = 0
        hp = k
        for pm in permut:
            if hp >= pm[0]:
                hp -= pm[1]
                cnt += 1
        answer = max(answer, cnt)
    return answer