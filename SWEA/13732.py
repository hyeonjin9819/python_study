import sys

sys.stdin = open("test.txt", "r")
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    li = []
    ans = []
    for j in range(N):
        data = list(map(str, input().split()))
        posList = [x for x in range(len(data[0])) if data[0][x] == '#']
        if posList:
            li.append(posList)

    for v in range(len(li)):
        if max(li[v]) - min(li[v]) == len(li)-1 and len(li[v]) == len(li):
            ans.append("yes")
        else:
            ans.append("no")

    if "no" in ans:
        print("#{} {}".format(i + 1, "no"))
    else:
        print("#{} {}".format(i + 1, "yes"))