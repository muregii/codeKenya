'''
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
 
Example 1:Input: s = "hello"
Output: "holle"

Example 2:Input: s = "leetcode"
Output: "leotcede"
'''

def reverseVowels(s):
    i = 0
    
    for letter in s:
        if letter == "a" or "e" or "i" or "o" or "u":
            temp = letter
            letter = temp
        else:
            i+=1
    return s
        