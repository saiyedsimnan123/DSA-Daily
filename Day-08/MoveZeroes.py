class Solution:
    def moveZeroes(self, nums):
        position = 0

        # Put all non-zero elements at the front
        for num in nums:
            if num != 0:
                nums[position] = num
                position += 1

        # Fill the remaining positions with zeroes
        while position < len(nums):
            nums[position] = 0
            position += 1
