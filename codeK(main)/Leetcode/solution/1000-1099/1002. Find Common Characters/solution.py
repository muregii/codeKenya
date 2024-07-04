class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        from collections import Counter

        # Initialize the counter with the first word
        common_count = Counter(words[0])
        
        # Intersect the counts with each subsequent word
        for word in words[1:]:
            common_count &= Counter(word)
        
        # Expand the counts into a list of characters
        result = []
        for char, count in common_count.items():
            result.extend([char] * count)
        
        return result