def solution(d, budget):
    sum = 0
    answer = 0
    d.sort()

    for data in d:
        sum += data
        if sum <= budget:
            answer += 1

    return answer