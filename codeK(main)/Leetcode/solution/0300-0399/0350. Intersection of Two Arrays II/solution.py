class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counts = {}
        for num in nums1:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        result = []
        for num in nums2:
            if num in counts and counts[num] > 0:
                result.append(num)
                counts[num] -= 1
        
        return result