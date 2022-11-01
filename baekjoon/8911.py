import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

move_types =['F', 'B', 'L', 'R']
# F: 한 눈금 앞으로
# B: 한 눈금 뒤로
# L: 왼쪽으로 90도 회전
# R: 오른쪽으로 90도 회전

for _ in range(T): # 한줄씩
    x, y = 0, 0
    dir = 1  # 1,2,3,4 -> 북 서 남 동
    xList = []
    yList = []
    plan = list(map(str, input()))
    for i in plan: # 한 줄의 하나의 갯수 씩
        if i == 'F':
            #print("F")
            nx = x + dx[dir-1]
            ny = y + dy[dir-1]
            x, y = nx, ny
            xList.append(x)
            yList.append(y)
            #print(x,y)
        elif i == 'B':
            #print("B")
            nx = x - dx[dir-1]
            ny = y - dy[dir-1]
            x, y = nx, ny
            xList.append(x)
            yList.append(y)
            #print(x, y)
        elif i == 'L':
            #print("L")
            if dir == 4:
                dir = 1
            else:
                dir += 1
            #print(dir)
        elif i == 'R':
            #print("R")
            if dir == 1:
                dir = 4
            else:
                dir -= 1
            #print(dir)
    #print(xList, yList)
    e = 0
    r = 0
    xMin = 0
    yMin = 0
    for xli in xList:
        if xli < 0:
            xMin = abs(min(xList))

    e = max(xList) + xMin
    #print(e)
    for yli in yList:
        if yli < 0:
            yMin = abs(min(yList))
    r = max(yList) + yMin
    #print(r)


    print(e*r)