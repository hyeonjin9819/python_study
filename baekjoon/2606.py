import sys
from collections import deque
sys.stdin = open("input.txt", "r")

o = int(input())
t = int(input())

cnt = 0

graph = [[] for _ in range(o+1)]

visit = [0] * (o+1)

for _ in range(t):
    n, m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)

for i in range(1, o+1):
    graph[i].sort()

print(graph)

# def dfs(v, cnt):
#     visit[v] = 1
#     cnt += 1
#     for nv in graph[v]:
#         if visit[nv] == 0: # 아직 방문 안함
#             visit[nv] = 1
#             cnt = dfs(nv, cnt)
#     return cnt
#
# print(dfs(1, 0) -1)

def bfs(v, cnt):
    visit = [0] * (o + 1)
    q = deque()
    visit[v] = 1 # 시작 방문처리
    q.append(v)


    while q:
        cnt += 1
        v = q.popleft()
        for nv in graph[v]:
            if visit[nv] == 0:
                visit[nv] = 1
                q.append(nv)
    return cnt

print(bfs(1,0)-1)