import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
t = int(input())

cnt = 0 # 갯수 확인용
right = 0 # 돌았는지 안돌았는지 확인용

while t >= 0:
    if t % 5 == 0: # 바로 5로 나눠지면?
        cnt += t //5
        print(cnt)
        right += 1
        break
    t -= 3
    cnt += 1

if right == 0:
    print(-1)
