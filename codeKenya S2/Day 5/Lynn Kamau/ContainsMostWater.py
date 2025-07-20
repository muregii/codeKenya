#Contains Most Water Leetcode Challenge
#You are given an integer array height of length n.
#There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#Find two lines that together with the x-axis form a container, such that the container contains the most water.
#Return the maximum amount of water a container can store.
#Notice that you may not slant the container.

def maxArea(height):
    n = len(height)
    max_area = 0

    for i in range(n):
        for j in range(i + 1, n):
            width = j - i
            h = min(height[i], height[j]) 
            area = width * h
            max_area = max(max_area, area)

    return max_area

#Example test
print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])) 