class Solution:

    def encode(self, strs):
        encoded = ""
        for s in strs:
            # Add length + delimiter + string
            encoded += str(len(s)) + "#" + s
        return encoded

    # Decodes a single string to a list of strings.
    def decode(self, s):
        res = []
        i = 0
        while i < len(s):
            j = i
            # Find the next '#' to extract the length
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            actual_str = s[j+1 : j+1+length]
            res.append(actual_str)
            i = j + 1 + length
        return res

solution = Solution()


original = ["neet", "code", "love", "you"]
encoded = solution.encode(original)
decoded = solution.decode(encoded)
print("Encoded:", encoded)   
print("Decoded:", decoded) 

