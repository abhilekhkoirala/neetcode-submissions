class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum_product = max(nums)
        current_minimum, current_maximum = 1, 1


        for n in nums:
            if n == 0:
                current_minimum, current_maximum = 1, 1 
                continue

            tmp = n*current_maximum
            current_maximum = max(n*current_maximum, n*current_minimum, n)
            current_minimum= min(tmp, n*current_minimum, n)
            
            maximum_product = max(maximum_product, current_maximum)
        return maximum_product 