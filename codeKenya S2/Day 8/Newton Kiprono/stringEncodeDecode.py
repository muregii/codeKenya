class Solution:

    def encode(self, strs: List[str]) -> str:
        if (len(strs) == 0): return "nullFlag"
        # join the list elements
        string = ""
        for s in strs:
          string += s + '#endFlag'
        return string

    def decode(self, s: str) -> List[str]:
        if (s == "nullFlag"): return []
        # tockenize the string
        output = s.split("#endFlag")
        return output[:-1]
if __name__=='__main__':
   sol = Solution()
   encodedStr = sol.encode(["The quick brown fox","jumps over the","lazy dog","1234567890","abcdefghijklmnopqrstuvwxyz"])
   decodedStr = sol.decode(encodedStr)
  #  print(encodedStr)
   print(decodedStr)
