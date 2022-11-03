import sys

sys.stdin = open("test.txt", "r")
input = sys.stdin.readline

T = int(input())

for i in range(T):
    data = list(input().split())
    cnt = 0
    stack = []

    for j in range(len(data[0])):
        stack.append(data[0][j])
        if data[0][j] == '(':
            if data[0][j+1] == ')' or data[0][j+1] == '|':
                cnt +=1
            else: continue
        elif data[0][j] == ')':
            if j == 0:
                break
            if data[0][j-1] == '|':
                cnt += 1
    print("#{} {}".format(i+1, cnt))
