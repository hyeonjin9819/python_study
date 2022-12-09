import sys
import math

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

a,b = list(map(int, input().split(' ')))

so = a*b

while b:
    mod = a%b
    a = b
    b = mod
    dae = a

ans = so // dae
print(dae)
print(ans)

# print(math.lcm(a,b))
# print(math.gcd(a,b))
