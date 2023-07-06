import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

t = int(input())

for i in range(t):
    stack = []
    data = str(input())

    for ele in data:
        if ele == "(":
            stack.append(ele)
        elif ele == ")":
            if len(stack) == 0:
                stack.append(')')
                break
            else:
                stack.pop()
    if len(stack) != 0:
        print('NO')
    else:
        print('YES')

