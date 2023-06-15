# 30분
def solution(n, a, b):
    answer = 0
    if (a > b):  # a,b 중 누가 큰 수인지 안정해져있음 -> 강제로 맞춘다.
        a, b = b, a

    for i in range(n):
        if (a % 2 == 1):  # a가 홀수인데
            if (a + 1 == b):
                answer += 1
                return answer
            else:  # 아직 못만난다.
                answer += 1
                a = a // 2 + 1  # 다음 차례 a의 참가자 번호가 바뀐다.
                # b는 짝수인지 홀수인지
                if (b % 2 == 1):  # b가 홀수면
                    b = b // 2 + 1
                else:
                    b = b // 2
        else:  # a가 짝수다
            if (a - 1 == b):  # 이렇게되면 끝!
                answer += 1
                return answer
            else:  # 아직 못만난다.
                answer += 1
                a = a // 2  # 다음 차례 a의 참가자 번호가 바뀐다.
                # b는 짝수인지 홀수인지
                if (b % 2 == 1):  # b가 홀수면?
                    b = b // 2 + 1
                else:
                    b = b // 2
