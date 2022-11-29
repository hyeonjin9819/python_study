import sys
sys.stdin = open("input.txt", "r")

T = int(input())
dic = []
ans = []

print(T)

data = list(map(int, input().split()))
print(data)

for idx, val in enumerate(data):
    dic.append((idx, val))

print(dic)
print(dic[0][0])