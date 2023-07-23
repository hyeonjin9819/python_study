import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
words = []
for i in range(n):
    words.append(input().strip())

words = sorted(list(set(words)))
words.sort(key=len)

for ele in words:
    print(ele)