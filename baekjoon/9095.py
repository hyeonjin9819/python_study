# 문제: 백준 9095번 1,2,3 더하기
# 정수 n이 주어졌을 때, n을 1,2,3의 합으로 나타내는 방법의 수를 구하는 프로그램
# 출력: 각 테스트 케이스마다, n을 1,2,3의 합으로 나타내는 방법의 수를 출력
# input.txt: 3 4 7 10 (첫 줄은 테스트 케이스 갯수)

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())

# sum은 합, n은 문제의 입력 값
def go(sum, goal):
    sum = 0
    count = 0
    if (sum > goal):
        return  # 정지조건?

    if (sum == goal):
        count += 1
        return  # 정지조건?

    if (sum < goal):
        now = 0  # 현재 값

        for i in (1, 4):
            print(i)
            print(n)
            print(now)
            #go(sum + i, n)
            #print(go(sum+i, n))
            now = now + go(sum+i, n)
            # print(now)
            #print(count)
        return now

for i in range(T):
    n = int(input())
    #print(n)
    go(0, n)

