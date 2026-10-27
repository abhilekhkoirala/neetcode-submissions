class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #left and right pointer
        left_pointer = 0 
        right_pointer = left_pointer + 1
        #intial profit 
        max_profit = 0

        #for pointer ending
        while right_pointer < len(prices):
            #prifit? calculation
            if prices[left_pointer] < prices[right_pointer]:
                profit = prices[right_pointer] - prices[left_pointer]
                max_profit = max(max_profit, profit)
            else:
                left_pointer = right_pointer
            
            right_pointer += 1

        return max_profit 
