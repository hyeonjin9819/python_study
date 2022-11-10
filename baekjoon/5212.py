import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
data = []
li = []
a = []

R, C = map(int, input().split())
print(R,C)
# arr = [[0] * C for _ in range(R)]
# print(arr)


for i in range(R):
    data = list(map(str, input().rstrip()))
    for ele in data:
        li.append(ele)
print(li)


for j in range(R*C):
    cnt = 0
    if li[j] == 'X':
        # if j - C > 0 and j + C < R * C:
        #     cnt += 1
        print("확인")
        print(j)
        if li[j-C] == '.':
            print("위")
            cnt += 1
            print(cnt)

        if j > (R-1) * C:
            continue
        elif li[j+C] == '.':
            print("아래")
            cnt += 1
            print(cnt)

        if li[j+1] == '.':
            print("오르쪽")
            cnt += 1
            print(cnt)

        if j %C == 0:
            print("왼쪽에 붙음")
            cnt += 1
        elif li[j-1] == '.':
            print("왼쪽")
            cnt += 1
            print(cnt)

        if cnt >=3:
            a.append(j)
    print(a)
    print("총")
    print(cnt)
    print(li)

for k in a:
    li[k] = '.'

print(li)
for q in range(1, R*C+1):
    if q%C == 0:
        print(li[q-1])
    else:
        print(li[q-1], end =" ")