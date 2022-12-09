import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

T = int(input())
data = list(map(int, input().split(' ')))
da = max(data)
cnt = 0

def prime_list(n):
    sieve= [True] * n
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    return [i for i in range(2,n) if sieve[i] == True]

for x in data:
    if x in prime_list(da+1):
        cnt += 1

print(cnt)