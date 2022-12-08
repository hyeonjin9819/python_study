import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

# 9명 중 7명 골라서 합이 100이면 완성
li = []
for i in range(9):
    li.append(int(input()))

val = sum(li) - 100

for a in range(9):
    for b in range(a+1, 9):
        if li[a] + li[b] == val:
            x = li[a]
            y = li[b]
            break
li.remove(x)
li.remove(y)
li.sort()
for c in li:
    print(c)