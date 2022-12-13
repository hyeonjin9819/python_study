import sys
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

a,b = map(int, input().split(' '))
li = []

for i in range(b+1):
    for j in range(i):
        li.append(i)

print(sum(li[a-1:b]))