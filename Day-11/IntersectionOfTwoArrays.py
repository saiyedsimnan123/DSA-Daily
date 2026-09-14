class Solution:
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        result = []

        for num in nums2:
            if num in set1:
                result.append(num)
                set1.remove(num)

        return result



solution = Solution()

print(solution.intersection([1, 2, 2, 1], [2, 2, 3]))
print(solution.intersection([4, 9, 5], [9, 4, 9, 8, 4]))
