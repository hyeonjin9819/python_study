from collections import deque
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visit = [0] * (n+1)

# 그래프에 값 넣기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

def dfs(v):
    print(v, end=' ')
    for nv in graph[v]:
        if visit[nv] == 0: # 아직 간적 없음?
            visit[nv] = 1
            dfs(nv)

visit[v] = 1
dfs(v)

print()

def bfs(v):
    q = deque()
    q.append(v)
    visit = [0] * (n+1)
    visit[v] = 1 # 첫 방문 처리

    while q:
        v = q.popleft() # 일단 한놈을 뽑음
        print(v, end=' ')
        for nv in graph[v]:
            if visit[nv] == 0:
                visit[nv] = 1
                q.append(nv)

bfs(v)