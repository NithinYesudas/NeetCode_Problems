class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cursum = 0
        for i in range(len(nums)):
            if cursum<0:
                cursum = 0

            cursum+=nums[i]
            max_sum = max(max_sum,cursum)
        return max_sum

        