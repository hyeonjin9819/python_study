def solution(numbers):
    answer = ''
    strAns = list(map(str, numbers))
    strAns = sorted(strAns, key=lambda x: (x * 4)[:4], reverse=True)
    answer = str(int(''.join(strAns)))

    return answer