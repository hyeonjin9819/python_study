import sys
sys.stdin = open("test.txt", "r")

input = sys.stdin.readline

T = int(input())

for i in range(T):
    num = int(input())
    data = list(map(int, input().split()))
    ans = 0
    li = []
    for j in range(1000):
        if data.count(data[j]) > ans:
            ans = data.count(data[j])
        else:
            continue
        li.append(data[j])
    print("#{} {}".format(i+1, li[-1]))
