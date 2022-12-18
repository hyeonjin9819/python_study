import sys
import pickle

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())

remove_set = {"a", "n", "t", "i", "c"}
cnt = 0
ans = 0
stackLen = []
ansLi = []
data_dict = set()

# 하나 더 고려 필요 -> 순서가 알파벳 갯수가 적은 것 부터 계산해야함
# 스택에 넣고 하나씩 계산해야하나?
# 완전탐색 -> 갯수로...?, 겹치는 알파벳이 있으면? => 둘다 확인?
# 가장 적은 것 순서로 보면서 겹치는거 지워나가기? 아니면 모두 확인

for i in range(N):
    if K < 5:
        print(0)
    else:
        data = list(set(str(input().rstrip("\n"))))
        li = [j for j in data if j not in remove_set]
        cnt += len(li)

        data_dict.add()
        print(li)
        print(cnt)

    #if len(data) <
    #print(data)