import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

white = []
black = []

for i in range(3):
    data = list(map(int, input().split()))
    if i == 1:
        white.append(data[1])
        black.append(data[0])
    else:
        white.append(data[0])
        black.append(data[1])

value = min(black) - min(white)

if abs(value) > 2:
    print(min(min(black),min(white))*2 +1)
else:
    print(min(black) + min(white))
