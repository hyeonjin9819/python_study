import sys
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline


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
