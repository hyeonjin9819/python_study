import sys
sys.stdin = open("test.txt", "r")
n = int(input())
x,y = 1,1
plans = input().split()

dx = [0,0,-1,-1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    print(plan)
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx <1 or ny <1 or nx >n or ny > n:
        continue
    x, y = nx, ny
print(x,y)


for idx, val in enumerate(data):
    dic.append((idx, val))

    a = [[] for _ in range(n + 1)]
    print("#{} {}".format(i+1, cnt))

posList = [x for x in range(len(data[0])) if data[0][x] == '#']
