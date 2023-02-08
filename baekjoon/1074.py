import sys

sys.stdin = open("input.txt", "r")

# N: 네모 칸, r: 행, c: 열
N, r, c = map(int, input().split())

ans = 0

# 계속 해당하는 분할을 찾아 쪼갬
while N:
    N -= 1
    # N-1 을 했기 때문에 중앙 현재 분할한 배열의 중간값
    gijun = 2 ** N
    # 행열이 사분할 중 어디에 해당하는지 확인
    # 1분할에 해당
    if r < gijun and c < gijun:
        ans += (gijun ** 2) * 0
    # 2분할에 해당
    elif r < gijun <= c:
        ans += (gijun ** 2) * 1
        c -= gijun
    # 3분할에 해당
    elif r >= gijun > c:
        ans += (gijun ** 2) * 2
        r -= gijun
    # 4분할에 해당
    else:
        ans += (gijun ** 2) * 3
        r -= gijun
        c -= gijun

print(ans)
