import sys
from itertools import combinations
sys.stdin = open("input.txt", "r")

N, S = map(int, input().split())
data = list(map(int, input().split()))
ans = 0

for i in range(N+1): # 전체를 더하는 조합도 생각해야하기 때문에 N+1
    full = list(combinations(data, i))
    for j in range(len(full)):
        # print(sum(full[j]))
        # print(full[j])
        if sum(full[j]) == S:
            ans += 1
# S가 0일때는 공집합과 겹쳐 계산되기 때문에 공집합의 갯수 1을 빼줘야함
if S == 0:
    ans -= 1

print(ans) #공집합 제거