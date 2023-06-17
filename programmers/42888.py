from collections import deque


def solution(record):
    answer = []
    dictname = dict()
    li = []
    dq = deque()

    # 닉네임을 확정해주는 딕셔너리
    for i in range(len(record)):
        li = record[i].split(' ')
        if li[0] != "Leave":  # Enter, Change만 확인하면 됨
            dictname[li[1]] = li[2]  # key: id, value: 닉네임(갱신가능)

    # answer에 들어갈 값을 raw 형태로 dq에 저장
    for j in range(len(record)):
        li = record[j].split(' ')
        if li[0] != "Change":
            dq.append(li[1])  # (인덱스 짝수) Enter, Leave 둘중 하나 들어감
            dq.append(li[0])  # (인덱스 홀수) 닉네임 들어감

    # 디큐에서 하나씩 뽑아서 문자열 만들어서 ans에 넣자 (디큐에는 Enter, Leave만 있음)
    for x in range(0, len(dq), 2):
        sentence = ''  # 들어갈 한 문장
        if (dq[x] in dictname):
            sentence += dictname[dq[x]] + "님이 "
        if (dq[x + 1] == "Enter"):  # Enter
            sentence += "들어왔습니다."
        else:  # Leave
            sentence += "나갔습니다."
        answer.append(sentence)
    return answer