import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())  # 4, 2
num = sorted(list(map(int, input().split())))

li = []

def dfs(cnt):
    if cnt == m:
        print(*li)
        return

    for i in range(len(num)):
        if num[i] not in li:
            li.append(num[i])
            dfs(cnt+1)
            li.pop()
dfs(0)

