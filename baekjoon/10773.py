import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())

stack = []
for i in range(n):
    a = int(input())
    if a == 0:
        stack.pop()
    else:
        stack.append(a)

sum =0
for ele in stack:
    sum += ele

print(sum)