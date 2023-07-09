import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())

num = [i for i in range(1, n+1)]
li = []

def dfs(idx, cnt):
    if cnt == m:
        print(*li)
        return

    for i in range(idx, len(num)):
        li.append(num[i])
        dfs(i, cnt +1)
        li.pop()

dfs(0, 0)
