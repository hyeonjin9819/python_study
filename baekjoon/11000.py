import sys
import heapq
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
N = int(input())
lessons = [list(map(int, input().split())) for _ in range(N)]

# 수업 시작 시간 기준으로 오름차순 정렬함
lessons = sorted(lessons, key=lambda x: x[0])

q = []

for lesson in lessons:
    if q and q[0] <= lesson[0]:
        heapq.heappop(q)
    heapq.heappush(q, lesson[1])

print(len(q))

# 시간초과

# T = int(input())
# li = []
# big = 0
#
# for _ in range(T):
#     s, t = map(int, input().split())
#     li.append(s)
#     li.append(t)
#     big = max(li)
#
# arr = [[0 for i in range(max(li)+1)] for j in range(T)]
#
# for a in range(T):
#     q = li[0]
#     w = li[1]
#     li.remove(q)
#     li.remove(w)
#     for b in range(q,w):
#         arr[a][b] = 1
#
# ans = []
# cnt = 0
# for p in range(big):
#     ans.append(cnt)
#     cnt = 0
#     for m in range(T):
#         if arr[m][p] == 1:
#             cnt += 1
# print(max(ans))
