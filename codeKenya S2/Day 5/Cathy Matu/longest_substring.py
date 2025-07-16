class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()        
        left = 0 
        max_len = 0           

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])  
                left += 1
            seen.add(s[right])        
            max_len = max(max_len, right - left + 1)

        return max_len
    
    
#Using given examples
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))  
print(sol.lengthOfLongestSubstring("bbbbb"))     
print(sol.lengthOfLongestSubstring("pwwkew"))    
