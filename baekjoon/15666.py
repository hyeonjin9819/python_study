import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))

li = []
ans = set()

def dfs(idx, cnt):
    if cnt == m:
        ans.add(tuple(li))
        return

    for i in range(idx, len(num)):
        li.append(num[i])
        dfs(i, cnt+1)
        li.pop()

dfs(0, 0)

for j in sorted(ans):
    print(*j)