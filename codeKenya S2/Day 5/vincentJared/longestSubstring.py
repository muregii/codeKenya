class Solution:
    def lengthofLongestSubstring(self, s: str)-> int:
        seen = set()
        left = 0
        ans = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                
            seen.add(s[right])
            ans = max(ans, right - left + 1)
            
        return ans
    
    
print(Solution().lengthofLongestSubstring("abcabcbb"))
print(Solution().lengthofLongestSubstring("bbbbb"))
print(Solution().lengthofLongestSubstring("pwwkew"))
print(Solution().lengthofLongestSubstring(""))
        