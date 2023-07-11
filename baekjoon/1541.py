import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
origin = str(*input().split())
data = list(origin.split("-"))

if len(data) >1: # -가 있는 경우
    if origin[0] == '-': #시작부터 음수인 경우
        first = 0
        a = data[1].split("+")
        for q in a:
            first += int(q)
        first = first* (-1)
        for i in range(2, len(data)):
            temp = 0
            ele = data[i].split("+")
            for j in ele:
                temp += int(j)
            first -= temp
        print(first)
    else: # 시작은 양수인 경우
        first = 0
        a = data[0].split("+")
        for q in a:
            first += int(q)
        for i in range(1, len(data)):
            temp = 0
            ele = data[i].split("+")
            for j in ele:
                temp += int(j)
            first -= temp
        print(first)
else:
    sum = 0
    ele = data[0].split("+")
    for j in ele:
        sum += int(j)
    print(sum)