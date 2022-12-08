import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

li = list(map(int, input().split(' ')))
val = li[0]
num = li[1]
ans = []

for i in range(1, val+1):
    if val % i == 0:
        ans.append(i)
if len(ans) < num:
    print(0)
else:
    print(ans[num-1])