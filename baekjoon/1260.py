# 문제: 백준 1260번 DFS와 BFS

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m, start = map(int, input().split()) # n: 정점의 갯수, m: 간선의 갯수
a = [[] for _ in range(n+1)]
check = [False] * (n+1) # 확인을 위한 플래그

# 인접 리스트
for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)

for i in range(n):
    a[i].sort()

# DFS
def dfs(x):
    global check
    check[x] = True
    print(x, end = ' ')
    for y in a[x]:
        if check[y] == False:
            dfs(y)

# BFS
def bfs(start):
    check = [False] * (n+1)
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for y in a[x]:
            if check[y] == False:
                check[y] = True
                q.append(y)

dfs(start)
print()
bfs(start)
