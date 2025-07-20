#Valid Anagram Leetcode Challenge
#Given two strings s and t, return true if t is an anagram of s and false otherwise.            

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counts = [0] * 26  # For 26 lowercase letters
    base = ord('a')

    for char in s:
        counts[ord(char) - base] += 1

    for char in t:
        counts[ord(char) - base] -= 1
        if counts[ord(char) - base] < 0:
            return False

    return True

# Example usage
if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))  
    print(is_anagram("rat", "car"))           
    print(is_anagram("listen", "silent"))     
    print(is_anagram("hello", "world"))      
    print(is_anagram("aabbcc", "abcabc"))   