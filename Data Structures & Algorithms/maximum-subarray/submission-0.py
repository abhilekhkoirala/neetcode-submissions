class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum_subarray = nums[0]
        current_sum = 0

        for n in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += n
            maximum_subarray = max(maximum_subarray, current_sum)
        
        return maximum_subarray

            
