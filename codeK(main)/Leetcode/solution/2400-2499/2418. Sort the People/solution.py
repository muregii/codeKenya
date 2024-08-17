class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        # Zip names and heights together and sort by heights in descending order
        people = sorted(zip(heights, names), reverse=True)
        
        # Extract and return the names from the sorted list
        return [name for height, name in people]