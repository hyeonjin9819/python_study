import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

T = int(input())
N = int(input())

data = []
li = []
cnt = 0
now = 1

for i in range(N):
    a = int(input())
    data.append(a)

for j in range(N):
    b = data[j-1]
    print(b)
    #print(data.index(b))
    data.remove(b)


print(data)
print(data[now])

