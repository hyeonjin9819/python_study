class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        li = []
        b = {}
        for data in strs:
            li.append(sorted(data))
        print(li)
        num = len(li)
        for item in strs:
            if item in b:
                b[item].append(item)
            else:
                b[item] = [item]
        print(list(b.values()))