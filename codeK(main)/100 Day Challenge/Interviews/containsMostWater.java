class Solution {
    public int maxArea(int[] height) {
        var left = 0;
        var right = height.length-1;
        var area  = 0;

        while(left < right){
            var minHeight = Math.min(height[left], height[right]);
            var width = right - left;
            area = Math.max(area, width * minHeight);

            if(height[left] < height[right]){
                left++;
            }else{
                right--;
            }

            
        }
        return area;
    }
}
