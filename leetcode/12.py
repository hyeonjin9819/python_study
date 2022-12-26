class Solution:
    def intToRoman(self, num: int) -> str:
        # ans = []
        # # 1000 단위 계산
        # if num // 1000 >0:
        #     for i in range(num//1000):
        #         ans.append("M")
        #         num -= 1000
        # # 100 단위 계산
        # if num // 100 == 9:
        #     ans.append("CM")
        #     num -= 900
        # elif num // 100 == 4:
        #     ans.append("CD")
        #     num -= 400
        # elif num // 500 > 0:
        #     ans.append("D")
        #     num -= 500
        # if num // 100 >0:
        #     for i in range(num//100):
        #         ans.append("C")
        #         num -= 100
        # # 10 단위 계산
        # if num // 10 == 9:
        #     ans.append("XC")
        #     num -= 90
        # elif num // 10 == 4:
        #     ans.append("XL")
        #     num -= 40
        # elif num // 50 > 0:
        #     ans.append("L")
        #     num -= 50
        # if num // 10 >0:
        #     for i in range(num//10):
        #         ans.append("X")
        #         num -= 10
        # # 1 단위 계산
        # if num == 9:
        #     ans.append("IX")
        #     num -= 9
        # elif num == 4:
        #     ans.append("IV")
        #     num -= 4
        # elif num // 5 > 0:
        #     ans.append("V")
        #     num -= 5
        # if num >0:
        #     for i in range(num):
        #         ans.append("I")
        #         num -= 1
        # return(''.join(ans))

    answer = ''
    symbols = [('M', 1000), ('D', 500), ('C', 100), ('L', 50), ('X', 10), ('V', 5), ('I', 1)]
    for i in range(len(symbols)):
        s, v = symbols[i][0], symbols[i][1]

        if v > num:
            continue

        if str(num)[0] == '4':
            answer += symbols[i][0] + symbols[i - 1][0]
            num -= symbols[i - 1][1] - symbols[i][1]
            continue
        if str(num)[0] == '9':
            answer += symbols[i + 1][0] + symbols[i - 1][0]
            num -= symbols[i - 1][1] - symbols[i + 1][1]
            continue

        answer += s * (num // v)
        num %= v
    return answer
