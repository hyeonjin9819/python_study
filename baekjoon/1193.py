import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

x = int(input())

# 몇번째 대각선인지 구하기
def findline(x):
    line = 0
    big = 0
    while x > big:
        line += 1
        big += line
    return line

val = findline(x)

sum = 0
for i in range(val):
    sum += i

# val +1 (줄수)가 짝수면 분모가 내림차순, 분자: 오름차순
# val +1 (줄수)가 홀수면 분모가 오름차순, 분자: 내림차순
for i in range(val+1):
    if (val +1) %2 == 1: # 홀수
        if i == (x-sum): # 줄 내에서의 순서
            print(''.join([str(i), "/", str(val-i+1)]))
    else: # 홀수
        if i == (x-sum):
            print(''.join([str(val-i+1), "/", str(i)]))
