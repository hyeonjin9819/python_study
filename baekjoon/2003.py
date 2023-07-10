import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int,input().split()))
sum = data[0]
start, end = 0, 0
cnt = 0

while start < n and end < n:
    if sum == m: # 일치하면?
        cnt += 1
        start += 1
        if start<len(data):
            end = start
            sum = data[start]
    elif sum > m: # 더 크면?
        start += 1
        if start<len(data):
            end = start
            sum = data[start] # 합 리셋
    else: # 더 작으면?
        end += 1
        if end < len(data):
            sum += data[end]

print(cnt)
