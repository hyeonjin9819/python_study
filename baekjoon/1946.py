import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 수
grade = dict()

for _ in range(T):
    N = int(input())  # 지원자 수
    ans = 1 # 가능한 합격자 수, 서류 1등은 합격
    big = 0 # 면접 최대값 저장을 위한 초기값
    for _ in range(N):
        a, b = map(int, input().split())
        grade.update({a:b})
    li = sorted(grade.items())
    big = li[0][1] # 정렬 후 면접에서의 최초 최대값
    for i in range(1, N): # 면접 부분 확인
        if li[i][1] < big: # 현재 면접 최대 값 big이 새로운 면접 등수보다 크면
            ans += 1 # 합격자 수 늘리고
            big = li[i][1] # # 면접 최대 값 big 교환
    print(ans)




