import sys
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

S = int(input())
hap = 0
i = 0
while hap <= S:
    i += 1
    hap += i
print(i-1)