# 프로그래머스 Lv2 더 맵게
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 기존 리스트 힙으로 변환

    while(len(scoville) >=2):
        if(scoville[0] < K): # 가장 작은 값이 K 보다 작으면
            ch = heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
            heapq.heappush(scoville, ch)
            answer += 1
        else:
            break
    # 다 해도 안되는 경우 -1 return
    if(scoville[-1] < K):
        return -1

    return answer