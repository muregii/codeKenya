class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        
        # Count occurrences of each number in arr1
        count = Counter(arr1)
        result = []
        
        # Append elements in the order of arr2
        for number in arr2:
            result.extend([number] * count.pop(number))
        
        # Sort remaining elements and append
        remaining_elements = sorted(count.elements())
        result.extend(remaining_elements)
        
        return result