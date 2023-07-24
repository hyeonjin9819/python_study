import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())

one = list(map(int,input().split()))
two = list(map(int,input().split()))

one = sorted(one)
two = sorted(two,reverse=True)

sum = 0
for i in range(n):
    sum += one[i] * two[i]

print(sum)