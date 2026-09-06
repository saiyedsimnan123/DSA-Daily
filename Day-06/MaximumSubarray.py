class Solution:
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            # Decide whether to start a new subarray
            # or continue the current one
            current_sum = max(nums[i], current_sum + nums[i])

            # Store the best sum found so far
            max_sum = max(max_sum, current_sum)

        return max_sum
