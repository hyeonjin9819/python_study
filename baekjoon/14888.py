import sys
import itertools

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

T = int(input())
data = list(map(int, input().split(' ')))
symbol = list(map(int, input().split(' ')))
symLi = []
ans = []

for i in range(max(symbol)):
    if symbol[0] > 0:
        symLi.append("+")
        symbol[0] -= 1
    if symbol[1] > 0:
        symLi.append("-")
        symbol[1] -= 1
    if symbol[2] > 0:
        symLi.append("*")
        symbol[2] -= 1
    if symbol[3]>0:
        symLi.append("%")
        symbol[3] -= 1

permu = itertools.permutations(symLi, T-1)
permuSet = list(set(list((permu))))


for i in range(len(permuSet)):
    temp = data[0]
    for j in range(T-1):
        if permuSet[i][j] == "+":
            temp += data[j+1]
        elif permuSet[i][j] == "-":
            temp -= data[j+1]
        elif permuSet[i][j] == "*":
            temp *= data[j+1]
        elif permuSet[i][j] == "%":
            if temp < 0:
                temp = abs(temp)
                temp //= data[j+1]
                temp -= 2*temp
            else:
                temp //= data[j+1]
    ans.append(temp)

print(max(ans))
print(min(ans))