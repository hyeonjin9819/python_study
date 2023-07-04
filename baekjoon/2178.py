import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []

# 어디로 갈 수 있음? -> 위, 아래, 왼쪽, 오른쪽
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    graph.append(list(map(int,input().rstrip())))

def bfs(x, y):
    q = deque()
    q.append((x, y)) # 좌표를 더해줌

    while q:
        print(x,y)
        x, y = q.popleft()

        for i in range(4): # 네방향 뒤지기
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph[n-1][m-1]

print(bfs(0,0))




