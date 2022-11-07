import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

A, B, C = map(int, input().split()) # 한 대 , 두 대, 세 대 가격

arr = [[0] * 100 for _ in range(3)]
sum = 0

for i in range(3):
    sta, end = map(int, input().split())
    for j in range(sta-1, end-1):
        arr[i][j] = 1

for j in range(100):
    if arr[0][j] == 1 and arr[1][j] == 1 and arr[2][j] == 1:
        sum += C*3
    elif arr[0][j] == 1 and arr[1][j] == 1 or arr[0][j] ==1 and arr[2][j] == 1 or arr[1][j] ==1 and arr[2][j] == 1:
        sum += B*2
    elif arr[0][j] == 1 or arr[1][j] ==1 or arr[2][j] == 1:
        sum += A*1

print(sum)