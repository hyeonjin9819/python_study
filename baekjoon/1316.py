import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
t = int(input())

cnt = 0

for i in range(t):
    li = []
    data = list(input())

    for ele in data:
        if ele in li: # 일단 리스트 안에 들어있는지 확인
            if li[-1] == ele:
                li.append(ele)
            else: break
        else:
            li.append(ele)

        if li == data:
            cnt += 1
print(cnt)
