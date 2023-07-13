import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data = sorted(data)

sum = 0
ans = 0

for i in range(len(data)+1):
    for j in range(0, i):
        sum = 0
        sum += data[j]
        ans += sum

print(ans)

