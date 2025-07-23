#Container with the most water
#Time complexity: O(n)
#Space complexity: O(1)
class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            curr_height = min(height[left], height[right])
            area = curr_height * width
            max_water = max(max_water, area)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water

print(Solution().maxArea([1,7,2,5,4,7,3,6]))  
print(Solution().maxArea([2,2,2]))           
print(Solution().maxArea([1,1]))              
print(Solution().maxArea([4,3,2,1,4]))      