import sys
import heapq

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
ans = 0
N = int(input())
data = []

# 주어진 데이터를 힙을 사용해 data라는 리스트 변수에 집어넣음
for _ in range(N):
    heapq.heappush(data, int(input()))

if N == 1:
    print(ans)
else:
    for i in range(N-1):
        one = heapq.heappop(data) #data에서 가장 작은 값을 뽑고 pop함
        two = heapq.heappop(data) #data에서 가장 작은 값을 뽑고 pop함
        ans += one + two # 두 값을 더함
        heapq.heappush(data, one+two) #더한 값을 다시 data에 집어넣음
    print(ans)