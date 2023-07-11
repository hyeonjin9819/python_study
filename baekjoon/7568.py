import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())

data = []

for i in range(n):
    ele = list(map(int, input().split()))
    data.append(ele)

for i in range(n):
    ans = 1
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            ans += 1
    print(ans, end=' ')



