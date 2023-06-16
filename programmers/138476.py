# import operator

def solution(k, tangerine):
    # groupby=list(set(tangerine))  -> 시간초과
    # 파이썬에서 요소마다 갯수를 세는 반복문
    #     for i in groupby:
    #         result[i]=tangerine.count(i)
    #     print(result)

    # 아래 코드로 수정
    result = dict()
    for i in tangerine:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1

    # value값이 많은 순으로 정렬
    # d1 = sorted(result.items(), key=operator.itemgetter(1), reverse =True)
    d1 = sorted(result.items(), key=lambda x: x[1], reverse=True)

    a = len(d1)
    cnt = 0

    for i in range(a):
        k -= d1[i][1]
        cnt += 1

        if k <= 0:  # k가 0보다 작아지면 리턴
            return cnt
