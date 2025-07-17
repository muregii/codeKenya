class Solution:

    # Encodes a list of strings to a single string.
    def encode(self, strs):
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    # Decodes a single string to a list of strings.
    def decode(self, s):
        res = []
        i = 0
        while i < len(s):
            j = i
            # Finding the delimiter '#' to extract the length
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            # Extract the actual string using the found length
            actual_str = s[j+1:j+1+length]
            res.append(actual_str)
            i = j + 1 + length
        return res
