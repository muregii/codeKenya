from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0
        for i, citation in enumerate(citations):
            if i + 1 <= citation:
                h_index = i + 1
            else:
                break
        return h_index
