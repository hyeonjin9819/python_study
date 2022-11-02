import sys

sys.stdin = open("test.txt", "r")
input = sys.stdin.readline

T = int(input())

for i in range(T):
    data = list(map(int, input().split()))
    data.remove(max(data))
    data.remove(min(data))
    average = round(sum(data) / len(data))
    print("#{} {}".format(i+1, average))