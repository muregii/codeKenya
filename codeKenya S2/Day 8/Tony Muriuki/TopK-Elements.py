class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 1: Building frequency map using plain dict
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        #2: Build buckets: index = frequency, value = list of nums with that freq
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for num in freq_map:
            freq = freq_map[num]
            buckets[freq].append(num)

        #3: Collecting top k frequent elements from the buckets (starting from highest freq)
        result = []
        for i in range(n, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
