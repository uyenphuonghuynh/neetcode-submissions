class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r= 0, 1
        result = 0
        while l < r and r < len(prices):
            if prices[r] > prices[l]:
                result = max(result, prices[r] - prices[l])
                r += 1
            else:
                l = r
                r += 1
        return result

