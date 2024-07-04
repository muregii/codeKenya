class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        
        # Count frequency of each character
        counts = Counter(s)
        length_of_palindrome = 0
        odd_found = False
        
        for count in counts.values():
            # Add pairs to the palindrome length
            length_of_palindrome += (count // 2) * 2
            # Check if there is an odd character count
            if count % 2 == 1:
                odd_found = True
        
        # If there is any odd character, we can place one in the middle
        if odd_found:
            length_of_palindrome += 1
        
        return length_of_palindrome