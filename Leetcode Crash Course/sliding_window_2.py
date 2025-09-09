"""Example 2: You are given a binary string s (a string containing only "0" and "1"). 
You may choose up to one "0" and flip it to a "1". 
What is the length of the longest substring achievable that contains only "1"?
"""
@staticmethod
def longest_substring_of_ones(s: str) -> int:
    left = 0
    count = 0
    ans = 0
    for right in range(len(s)):
        if s[right] == '0':
            count += 1
        while count > 1:
            if s[left] == '0':
                count -=1
            left +=1

        ans = max(ans, right - left + 1)
    
    return ans

string_s = "1101101"
result = longest_substring_of_ones(string_s)
print(result)



