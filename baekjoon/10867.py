import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())

data = list(map(int, input().split()))
data = list(set(data))
data.sort()

for i in data:
    print(i, end = ' ')