import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline


data = list(input())

stack = []
ans = 1
result = 0

for i in range(len(data)):
    if data[i] == '(':
        ans *= 2
        stack.append(data[i])
    elif data[i] == '[':
        ans *= 3
        stack.append(data[i])
    elif data[i] == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if data[i-1] == '(':
            result += ans
        ans //= 2
        stack.pop()
    elif data[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if data[i-1] == '[':
            result += ans
        ans //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(result)
