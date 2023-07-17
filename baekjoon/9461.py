import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())

data =[]
for i in range(n):
    data.append(int(input()))

p = []
p.append(1)
p.append(1)
p.append(1)

for i in range(3,max(data)):
    p.append(p[i-3] + p[i-2])

for j in data:
    print(p[j-1])

