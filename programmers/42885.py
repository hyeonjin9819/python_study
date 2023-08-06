from collections import deque

class Something:
    def solution(self):
        people = [60, 60, 51, 51, 100]
        limit = 100
        answer = 0
        maxValue = 0
        dq = deque()
        peopleCl = people.copy()

        for i in range(len(people)):
            if (len(peopleCl) == 0):
                print("드디어 이제 혼자")
                print(answer)
                return answer
            if(len(people) == 1):
                print("혼자야")
                print(1)
                return 1
            if (limit - people[i] < 40):  # 혼자밖에 탈 수 없는 경우
                print("초과")
                peopleCl.remove(people[i])
                answer += 1
            else:  # 두 명이 탈 수 있는 경우
                print("탈수는 있음!")
                if (len(peopleCl) == 1):  # 두 명이 탈 수 있는 무게지만 혼자밖에 안남은 경우 +1을 해주고 Return
                    print("탈수는 있지만 남은게 하나뿐")
                    print(answer)
                    return answer + 1
                else:
                    for j in range(i + 1, len(people)):
                        if (people[i] + people[j] <= limit and people[i] + people[j] > maxValue):
                            print("짝이 있음")
                            maxValue = people[i] + people[j]
                            dq.append(people[i])
                            dq.append(people[j])
                        elif people[i] + people[j] >= limit:
                            print("탈려햇는데 가벼운 애가 없음")
                            print(peopleCl, people[i])
                            peopleCl.remove(people[i])
                            print("그래서 그냥 지우고 태움")
                            #print(peopleCl)
                            answer +=1
                            continue
                print(dq)
                #peopleCl.remove(dq.pop())
                #peopleCl.remove(dq.pop())
                answer += 1

s = Something()
s.solution()

