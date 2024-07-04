#Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
# 
#Example 1:Input: s = "abc", t = "ahbgdc"
#Map = [a -{0} h ->{1} b->{2} g ...]
#indices = [0]
#Output: true
#
#Example 2:Inputx: s = "axc", t = "ahbgdc"
#[1,2,3,4,5,8,6] -> sort -> [1, 2, 3,4, 5,6,8] log(n)
#Output: false
#
# 
#Constraints:
#0 <= s.length <= 100
#0 <= t.length <= 104
#s and t consist only of lowercase English letters.

# t = "abc" a ->  [0] b -> [1] c ->[2]
def subsequence(s, t):
    i = j = 0
    #abd abcd
    while j < len(t):
        if i < len(s) and s[i] == t[j]:
            i+=1
        j+=1
    return i == len(s)


    
    
test_cases = [
    ("abc", "ahbgdc"),  # True: "abc" is a subsequence of "ahbgdc"
    ("axc", "ahbgdc"),  # False: "axc" is not a subsequence of "ahbgdc"
    ("", "ahbgdc"),     # True: Empty string is a subsequence of any string
    ("abc", ""),        # False: Non-empty string cannot be a subsequence of an empty string
    ("ace", "abcde")    # True: "ace" is a subsequence of "abcde"
]

# Testing the function
for index, (s, t) in enumerate(test_cases):
    result = subsequence(s, t)
    print(f"Test Case {index + 1}: subsequence({s}, {t}) = {result}")