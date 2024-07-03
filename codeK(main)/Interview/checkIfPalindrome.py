
def checkPalindrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        #racecar
        if(s[left] != s[right]):
            return False
        left+=1
        right -=1
                 
    return True 

test_strings = ["racecar", "madam", "level", "hello", "world", "a", "ab", "", "Aba", "abba"]

for s in test_strings:
    result = checkPalindrome(s)
    print(f"Is {s} a palindrome? {result}")