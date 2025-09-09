#Given a string s, find the length of the longest substring without duplicate characters.
class Solution:  # Defines a class to group the solution method
    def lengthOfLongestSubstring(self, s: str) -> int:  # Returns length of longest substring without repeats
        left = 0  
        max_length = 0  # Tracks the maximum window size found so far
        last_seen_index = {}  # Maps character -> most recent index it appeared at
        for right, ch in enumerate(s):  # Expand window by moving right pointer over each character
            if ch in last_seen_index and last_seen_index[ch] >= left:  # If char repeated within current window
                left = last_seen_index[ch] + 1  # Move left just past the previous occurrence
            last_seen_index[ch] = right  # Update last seen position of current character
            max_length = max(max_length, right - left + 1)  # Update best length with current window size
        return max_length  # Return the length of the longest valid window found
    
solution = Solution()  # Create an instance of Solution
print(solution.lengthOfLongestSubstring("abcabcbb"))  # Example run: prints 3
    
    
