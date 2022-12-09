import sys

sys.stdin =open("input.txt", "r")

input = sys.stdin.readline

T = int(input())

for i in range(T):
    data = list(map(int, input().split(' ')))
    data.sort()
    print(data[7])