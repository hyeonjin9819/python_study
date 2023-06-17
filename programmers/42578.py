def solution(clothes):
    dict = {}
    li = []
    cnt = 1

    for i in range(len(clothes)):  # key만
        dict[clothes[i][1]] = []

    for i in range(len(clothes)):  # value 넣기
        dict[clothes[i][1]].append(clothes[i][0])

    for i in range(len(dict.values())):
        li = list(dict.values())
        cnt *= len(li[i]) + 1

    return cnt - 1