import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n,m = list(map(int, input().split()))

data = []

for i in range(n):
    a = int(input())
    if a <= m:
        data.append(a)

data = sorted(data, reverse=True)

cnt = 0
i =0

while m != 0:
    if m // data[i] >0:
        cnt += m // data[i]
        m %= data[i]
    else:
        i += 1

print(cnt)