import sys
import re
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

# import re 사용시 코드 짧아져 수정

while True:
    data = input()
    if data == 'end':
        break
    case1 = len(re.findall('[aeiou]', data)) != 0
    case2 = len(re.findall('[aeiou]{3}|[^aeiou]{3}', data)) == 0
    case3 = len(re.findall('([a-df-np-z])\\1', data)) == 0

    if case1 and case2 and case3:
        print(f'<{data}> is acceptable.')
    else:
        print(f'<{data}> is not acceptable.')