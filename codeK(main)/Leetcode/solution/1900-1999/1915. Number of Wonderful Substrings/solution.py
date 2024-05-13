class Solution(object):
    def wonderfulSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Initialize count for empty substring and bitmask for the empty string
        count = 0
        bitmask = 0
        # Dictionary to store the frequency of each bitmask
        freq = {0: 1}
        
        for char in word:
            # Update the bitmask by flipping the bit corresponding to the current character
            bitmask ^= 1 << (ord(char) - ord('a'))
            
            # If this bitmask has been seen before, add its frequency to the count
            count += freq.get(bitmask, 0)
            
            # Check for wonderful substrings with one odd character
            for i in range(10):
                # Flip each bit to check for substrings with one odd character
                count += freq.get(bitmask ^ (1 << i), 0)
            
            # Update the frequency dictionary for the current bitmask
            freq[bitmask] = freq.get(bitmask, 0) + 1
        
        return count