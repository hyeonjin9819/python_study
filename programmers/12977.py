# level 1 소수만들기
from itertools import combinations

def solution(nums):
    answer = 0
    for i in list(combinations(nums, 3)):
        sum = i[0] + i[1] + i[2]
        if ck_prime_number(sum) == True:
            answer += 1
    return answer


def ck_prime_number(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
