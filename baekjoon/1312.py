import sys
import math

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

A, B, N = map(int, input().split(' '))

for i in range(N+1):
    ans = A //B
    A = A%B * 10
print(ans)
