#Assignment 4: 125. Valid Palindrome
#A phrase is a palindrome if:
# 1. After converting all uppercase letters into lowercase letters
# 2. Removing all non-alphanumeric characters
# 3. It reads the same forward and backward. 
#Given a string s, return true if it is a palindrome, or false otherwise.


def isPalindrome(s: str) -> bool:
    cleaned = ""  

    for char in s:  
        if char.isalnum():  
            cleaned += char.lower()  

    reversed_cleaned = cleaned[::-1]  
    return cleaned == reversed_cleaned  

# Example usage
if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))  

