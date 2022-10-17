# 문제: 백준 9095번 1,2,3 더하기
# 정수 n이 주어졌을 때, n을 1,2,3의 합으로 나타내는 방법의 수를 구하는 프로그램
# 출력: 각 테스트 케이스마다, n을 1,2,3의 합으로 나타내는 방법의 수를 출력
# input.txt: 3 4 7 10 (첫 줄은 테스트 케이스 갯수)

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())
count = 0

# sum은 합, n은 문제의 입력 값
def go(sum, n):
    if (sum > n): # 수의 합이 목표 값을 넘어가면 함수 종료
        return

    elif(sum == n): #  수의 합이 목표 값과 같아지면 성공 횟수 +1
        global count
        count += 1
        return

    else:
        for i in range(1, 4):
            go(sum+i, n)

for i in range(T):
    n = int(input())
    go(0, n)
    print(count)
    count = 0
