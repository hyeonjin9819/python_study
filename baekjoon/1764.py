import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n,m = list(map(int, input().split()))

listen = []
see = []
for i in range(n+m):
    a = input().rstrip()
    if i <= n-1:
        listen.append(a)
    if i >= n+1:
        see.append(a)

ans = []
for ele in listen:
    if ele in see:
        ans.append(ele)

print(len(ans))
for a in sorted(ans):
    print(a)