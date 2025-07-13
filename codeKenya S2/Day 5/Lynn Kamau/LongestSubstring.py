# Assignment 5: 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s: str) -> int:
    current_substring = ""
    max_length = 0

    for char in s:
        if char in current_substring:
            index = current_substring.index(char)
            current_substring = current_substring[index + 1:]
        current_substring += char
        if len(current_substring) > max_length:
            max_length = len(current_substring)

    return max_length

# Example usage:
if __name__ == "__main__":      
    print(lengthOfLongestSubstring("abcabcbb"))  
    print(lengthOfLongestSubstring("pwwkew"))      
    print(lengthOfLongestSubstring("bbbbbb"))      
    print(lengthOfLongestSubstring(""))            