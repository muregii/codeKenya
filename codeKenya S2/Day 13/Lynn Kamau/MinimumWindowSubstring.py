# Minimum Window Substring
# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".
# You may assume that the correct output is always unique.

def min_window(s, t):
    if not s or not t:
        return ""
    need = {}
    for c in t:
        need[c] = 1 + need.get(c, 0)
    missing = len(t)
    left = start = end = 0
    for right, ch in enumerate(s, 1):
        if need.get(ch, 0) > 0:
            missing -= 1
        need[ch] = need.get(ch, 0) - 1
        if missing == 0:
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            if end == 0 or right - left < end - start:
                start, end = left, right
            need[s[left]] += 1
            missing += 1
            left += 1
    return s[start:end]

# usage
print(min_window( "OUZODYXAZV", "XYZ"))

# Time Complexity: O(n)
# Space Complexity: O(n)
