import sys
sys.stdin = open("book.txt", "r")

input = sys.stdin.readline
N, M, K = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
ans = 0

while M>0:
    for i in range(K):
        ans += max(data)
        M -= 1
    ans += data[-2]
    M -= 1
print(ans)