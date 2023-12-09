class Solution {
    public int maxArea(int[] height) {
        var left = 0;
        var right = height.length-1; 
        var area = 0;

        while (left < right){
            var minimumHeight = Math.min(height[left], height[right]);
            var width = right - left;
            var currentArea = width * minimumHeight;
            area = Math.max(area, currentArea);

            if(height[left] < height[right]){
            left++;
            }else{
            right--;
            }
          
        }
        return area;

    }
}