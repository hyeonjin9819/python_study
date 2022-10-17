# 문제: 백준 1759 암호 만들기
# 출력: 각 줄에 하나씩, 사전식으로 가능성 있는 암호를 모두 출력한다.

# 서로 다른 L개의 알파벳 소문자로 구성
# 최소 한 개의 모음 (a,e,i,o,u) / 최소 두개의 자음으로 구성, 중복 X
# 증가하는 순서로 배열 -> abc(O), bac(x)

# input.txt: 4 6 // a t c i s w

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


# 일단 자릿수에 맞는 암호를 만들어주는 함수
def make(L, list, password, i):
    # 정답인 경우
    if len(password) == int(L):
        if check(password):
            print(password)
    # 불가능한 경우 -> 종류
    elif i >= len(list):
        return
    # 다음 경우 (i번째를 사용하는 경우와 사용하지 않는 경우)
    else:
        make(L, list, password + list[i], i + 1)
        make(L, list, password, i + 1)


# 자음과 모음 갯수가 조건에 일치하는지 확인시켜주는 함수
def check(password):
    ja = 0
    mo = 0
    for j in password:
        if j in "aeiou":
            mo += 1
        else:
            ja += 1
    return ja >= 2 and mo >= 1


L, C = input().split()  # L: 암호 구성 갯수, C: 가능한 알파벳 갯수
list = input().split()
list.sort()  # .sort(): 알파벳 정렬
make(L, list, "", 0)
