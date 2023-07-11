import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
data = sorted(data)
x = int(input())

# 시간초과

# sum = data[0]
# start, end = 0, 0
# cnt = 0


# while start < n and end < n:
#     print(start, end, "sum= ", sum)
#     if sum > x: # 넘으면 다음으로 패스
#         start += 1
#         if start < len(data):
#             end = start
#             sum = data[start]
#     elif sum == x: # 일치
#         print("일치", start, end)
#         if start != end: # 두 수를 합쳐서 x와 같은 경우
#             cnt += 1
#             start += 1
#         else:  # 그냥 그 숫자 자체가 x와 같은 경우
#             start += 1
#         if start < len(data):
#             end = start
#             sum = data[start] # 합 리셋
#     else: # 불일치
#         sum = data[start]
#         end += 1
#         if end < len(data):
#             sum += data[end]
#         else:
#             start += 1
#             end = start
#             if start < len(data):
#                 sum = data[start]
#
# print(cnt)

print(data)
start, end = 0, n-1
cnt = 0

while start < end:
    sum = data[start] + data[end]
    if sum == x:
        cnt += 1
        start += 1
    elif sum < x:
        start += 1
    else:
        end -= 1
print(cnt)


