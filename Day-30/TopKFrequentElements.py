from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        frequency = Counter(nums)

        return [num for num, count in frequency.most_common(k)]
