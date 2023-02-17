from collections import deque


def solution(begin, target, words):
    # 타켓이 words에 없으면 무조건 변환 불가
    if target not in words:
        return 0

    # 둘이 변환 가능한지 아닌지 알려주는 함수
    def possible(one, two):
        wordCnt = 0
        for i in range(len(one)):
            # 위치가 똑같아야함 / 한번에 하나만 바꿀수 있으니까
            if one[i] != two[i]:
                wordCnt += 1
        if wordCnt == 1:
            return True
        else:
            return False

    def bfs():
        queue = deque()
        # 처음엔 begin, 0
        queue.append((begin, 0))

        while queue:
            print(queue)
            data, cnt = queue.popleft()
            print(data, cnt)
            for word in words:
                # 바꿀 수 있는지 확인
                if possible(data, word) == True:
                    if word == target:
                        return cnt + 1
                    else:
                        queue.append((word, cnt + 1))

    answer = bfs()
    return answer