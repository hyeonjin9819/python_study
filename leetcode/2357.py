class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        count = 0

        a = []

        while (1):
            for i in range(len(nums)):
                if nums[0] == 0:
                    if (len(nums) == 0):
                        nums.remove(0)
                        return count
                    else:
                        nums.remove(0)
                        count = count + 1
                        continue
                else:
                    print(nums)
                    small = nums[0]
                    print(nums[i - 1] - small)



