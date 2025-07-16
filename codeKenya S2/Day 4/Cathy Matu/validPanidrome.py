class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer if not alphanumeric
            while left < right and not s[left].isalnum():
                left += 1
            # Move right pointer if not alphanumeric
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare characters in lowercase
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))  
print(sol.isPalindrome("race a car"))                     
print(sol.isPalindrome(" "))                               
