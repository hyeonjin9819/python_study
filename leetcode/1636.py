class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        a = []
        print(Counter(nums).most_common())
        c = 0  # value
        b = 0  # key
        d = []
        answer = []
        global i
        i = 0
        collection = Counter(nums).most_common()
        print(collection)

        for i in range(len(collection)):
            print(i)
            print("zzzzzzzzzzz")
            key = collection[i][0]
            value = collection[i][1]
            print(key, value)
            print(b, c)

            if value != c:
                print(a)
                for j in range(value):
                    a.append(key)
                print(a)
                print("kkkkk")
                if i + 2 < len(collection):
                    b = collection[i + 2][0]
                    c = collection[i + 2][1]
                else:
                    b = 0
                    c = 0
                print(b, c)
                print(a)

            # value가 다음 나올 value인 c와 같다면
            elif value == c:
                d = []
                for _ in range(value):
                    d.append(key)  # 새로운 배열 d에 key 값을 저장
                print(d)  # d는 새로운 배열 -> 같은 value를 가진 키들을 모아주는 역할

                if i + 2 < len(collection):
                    b = collection[i + 2][0]
                    c = collection[i + 2][1]
                else:
                    b = 0
                    c = 0
                a += d
            print("aaaaaaa")
            print(d)
            # d.sort()
            # print(d)
            # print(a+d)
            # a += d
            print("answer")
        a.reverse()
        print(a)
        return a
