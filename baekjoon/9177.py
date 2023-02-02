import sys
from collections import deque

input = sys.stdin.readline


def bfs(words):
    A, B, C = words
    Q = deque([(len(A), len(B), len(C))])
    visited = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

    while Q:
        aa, bb, cc = Q.popleft()
        if aa == bb == cc == 0:
            return True
        elif cc == 0:
            return False
        if aa > 0 and A[aa - 1] == C[cc - 1] and visited[aa - 1][bb] == 0:
            visited[aa - 1][bb] = 1
            Q.append([aa - 1, bb, cc - 1])
        if bb > 0 and B[bb - 1] == C[cc - 1] and visited[aa][bb - 1] == 0:
            visited[aa][bb - 1] = 1
            Q.append([aa, bb - 1, cc - 1])
    else:
        return False

n = int(input())
for i in range(n):
    words = list(map(str, input().split()))
    if bfs(words):
        print(f"Data set {i + 1}: yes")
    else:
        print(f"Data set {i + 1}: no")