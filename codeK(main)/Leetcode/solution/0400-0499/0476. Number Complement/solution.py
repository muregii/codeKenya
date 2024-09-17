class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Step 1: Determine the bit length of num
        bit_length = num.bit_length()
        
        # Step 2: Create a mask with all 1's of the same length as num
        mask = (1 << bit_length) - 1
        
        # Step 3: XOR num with the mask to flip its bits
        return num ^ mask