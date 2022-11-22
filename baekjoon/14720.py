import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())
data = list(map(int, input().split(" ")))
cnt = 0

for i in range(T):
    if data[i] == cnt % 3:
        cnt += 1

print(cnt)

