# Find Median From Data Stream Leetcode Challenge
# The median is the middle value in a sorted list of integers. For lists of even length, there is no middle value, so the median is the mean of the two middle values.
# For example:
# For arr = [1,2,3], the median is 2.
# For arr = [1,2], the median is (1 + 2) / 2 = 1.5
# Implement the MedianFinder class:
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far.

import heapq

class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def add_num(self, num):
        heapq.heappush(self.small, -num)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2

# usage
mf = MedianFinder()
mf.add_num(1)
mf.add_num(2)
print(mf.find_median()) 
mf.add_num(3)
print(mf.find_median())

# Time Complexity: O(log n) for add_num, O(1) for find_median
# Space Complexity: O(n)
