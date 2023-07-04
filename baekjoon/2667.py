import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
t = int(input())

graph = []

for _ in range(t):
    graph.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global cnt
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4): # 네 방향 확인
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < t and 0 <= ny < t and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
    return cnt

li = []

for i in range(t):
    for j in range(t):
        cnt = 0
        if graph[i][j] != 0: # 집이 있는 경우 (1)일때만 진행
            ans = bfs(i, j)
            if ans != 0:
                li.append(ans)

print(len(li))
for ele in sorted(li):
    if ele == 1:
        print(1)
    else:
        print(ele-1)
