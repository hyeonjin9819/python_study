import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())

num = [i for i in range(1, n+1)]
li = []

def dfs(cnt):
    if cnt == m:
        print(*li)
        return

    for i in range(len(num)):
        li.append(num[i])
        dfs(cnt +1)
        li.pop()

dfs(0)
