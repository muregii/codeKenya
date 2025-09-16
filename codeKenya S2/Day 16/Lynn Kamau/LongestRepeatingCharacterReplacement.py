# Longest Repeating Character Replacement Leetcode Challenge
# You are given a string s consisting of only uppercase english characters and an integer k. 
# You can choose up to k characters of the string and replace them with any other uppercase English character.
# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

def character_replacement(s, k):
    count = {}
    left = 0
    maxf = 0
    res = 0
    for right in range(len(s)):
        count[s[right]] = 1 + count.get(s[right], 0)
        maxf = max(maxf, count[s[right]])
        while (right - left + 1) - maxf > k:
            count[s[left]] -= 1
            left += 1
        res = max(res, right - left + 1)
    return res

# Example Usage
print(character_replacement("XYYX", 2))
print(character_replacement("AAABABB", 1)) 


# Time Complexity: O(n)
# Space Complexity: O(26) ≈ O(1)
