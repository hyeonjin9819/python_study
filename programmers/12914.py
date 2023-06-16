def solution(n):
    a =1
    b =1
    if n == 1:
        return 1 % 1234567
    elif n==2:
        return 2 % 1234567
    else: # 피보나치
        for i in range(1,n+1):
            a,b = b, a+b
        return a % 1234567
