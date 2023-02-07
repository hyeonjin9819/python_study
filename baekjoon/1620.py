import sys
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

N, M = map(int, input().split())
dic = {} #정보 저장을 위한 빈 딕셔너리
reverse_dic = {}

for i in range(N):
    data = input().split()
    dic[i] = data[0] # 포켓몬 인덱스, 이름 저장

 # 시간복잡도 줄이기 위해 key, value 뒤집은 딕셔너리 생성
reverse_dic = dict(map(reversed, dic.items()))

for j in range(M):
    val = input().split()
    if val[0].isalpha(): #찾아야하는 값이 알파벳이면
        print(reverse_dic.get(val[0])+1)  # 뒤집은 딕셔너리에서 key로 value 찾기
    else: # 찾아야하는 값이 숫자면
        #print(val[0])
        valInt = int(val[0])
        print(dic.get(valInt -1)) # key로 value 찾기
