import sys

sys.stdin = open("test.txt", "r")
input = sys.stdin.readline

T = int(input())
correct = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(T):
    cnt = 0
    data = list(input().split())
    for j in range(len(data[0])):
        if data[0][j] == correct[j]:
            cnt += 1
        else:
            break
    print("#{} {}".format(i + 1, cnt))