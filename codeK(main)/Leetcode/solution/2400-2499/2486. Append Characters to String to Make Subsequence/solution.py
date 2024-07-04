class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        t_index = 0
        s_length, t_length = len(s), len(t)
        
        for char in s:
            if t_index < t_length and char == t[t_index]:
                t_index += 1
        
        return t_length - t_index