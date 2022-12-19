import sys
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

# n은 세로, m 은 가로
n, m = map(int, input().split())
data = list(input().split())
box = [[0]*m for i in range(n)]

# 주어진 박스에는 모두 1을 채운다
for i in range(m):
    for j in range(int(data[i])):
        box[j][i] =1

origin = box
print(box)

big = data[0]
now = 0
cnt = 0
for i in range(1,m):
    print(i)
    if data[i] > big: # 새로운 기둥 세우기
        if i != m-1:
            big = data[i]
            now = i # 가장 큰 애의 인덱스

        else:
            print("확인마지막", i)
            print("들어옴?")
            print(now)
            for j in range(i):
                print("ddd")
                for p in range(now, i):
                    if box[j][p] == 0:
                        cnt += 1
                        box[j][p] = 1
                    box[j][p] = 1
                    print(box)
    else:
        print("확인", i)
        if data[i] > data[i-1]:
            print("들어옴?")
            print(now)
            for j in range(int(data[i])):
                for p in range(now,i):
                    if box[j][p] == 0:
                        cnt += 1
                        print("증가요")
                        box[j][p] = 1
                    box[j][p] = 1
                    print(box)

print(cnt)