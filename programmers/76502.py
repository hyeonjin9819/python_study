from collections import deque


def solution(s):
    dq = deque(s)
    cnt = 0  # 만약에 괄호 중 하나라도 완성되면 +1 될 것

    for i in range(len(s)):
        if i == 0:
            dq = dq
        else:
            pre = dq.popleft()
            dq.append(pre)

        stack = []  # 스택
        stack.append(dq[0])

        for i in range(1, len(dq)):
            if len(stack) == 0:
                stack.append(dq[i])
            elif stack[-1] == "(" and dq[i] == ")":
                stack.pop()
            elif stack[-1] == "{" and dq[i] == "}":
                stack.pop()
            elif stack[-1] == "[" and dq[i] == "]":
                stack.pop()
            else:
                stack.append(dq[i])

        if (len(stack) == 0):
            cnt += 1
        else:
            continue

    return cnt