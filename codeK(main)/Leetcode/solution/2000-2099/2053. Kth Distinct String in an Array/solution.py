class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        # Step 1: Count frequencies
        frequency = {}
        for string in arr:
            frequency[string] = frequency.get(string, 0) + 1
        
        # Step 2: Find the kth distinct string
        distinct_count = 0
        for string in arr:
            if frequency[string] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return string
        
        # If fewer than k distinct strings exist
        return ""