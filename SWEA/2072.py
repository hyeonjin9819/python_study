# 홀수만 더하기
import sys

sys.stdin = open("test.txt", "r")
input = sys.stdin.readline

T = int(input())
li = []
a = 0

for i in range(T):
    li = list(input().split(" "))
    sum = 0
    for j in range(10):
        a = int(li[j])
        if a % 2 == 1:
            sum += a
        else:
            continue
    print("#{} {}".format(i+1, sum))
