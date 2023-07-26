import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())

q = deque()

for i in range(n):
    data = list(map(str, input().split()))
    if len(data)>1:
        if data[0] == "push_front":
            q.appendleft(data[1])
        elif data[0] == "push_back":
            q.append(data[1])
    else:
        if data[0] == "pop_front":
            if len(q) == 0:
                print(-1)
            else:
                print(q.popleft())
        elif data[0] == "pop_back":
            if len(q) == 0:
                print(-1)
            else:
                print(q.pop())
        elif data[0] == "size":
            print(len(q))
        elif data[0] == "empty":
            if len(q) == 0:
                print(1)
            else:
                print(0)
        elif data[0] == "front":
            if len(q) == 0:
                print(-1)
            else:
                print(q[0])
        elif data[0] == "back":
            if len(q) == 0:
                print(-1)
            else:
                print(q[-1])
