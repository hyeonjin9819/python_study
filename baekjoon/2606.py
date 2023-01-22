import sys

sys.stdin = open("input.txt", "r")

T = int(input())
N = int(input())

graph = [[] for i in range(T+1)]
visited = [0] * (T+1)

for i in range(N):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(num):
    visited[num] = 1
    for nx in graph[num]:
        if visited[nx] == 0:
            dfs(nx)

dfs(1)
print(sum(visited)-1)
