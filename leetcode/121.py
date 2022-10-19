class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        is_sorted = (sorted(prices)[::-1] == prices)  # 내침차순이면 True, 아니면 False
        profit = 0
        if is_sorted == True:
            print(0)
            return
        else:
            profit = 0
            small = prices[0]
            big = prices[0]
            profit = []
            print(min(prices))
            for i in range(len(prices)):
                minNum = min(prices)
                maxNum = max(prices)
                profit.append(maxNum - minNum)
            print(profit)