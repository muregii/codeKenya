//Recorded video of the interview: https://duke.zoom.us/rec/share/RN6ZUwd19FnW6Kc37KygD9l0EDhk7ttvqamfw-_sArZJb-aVyqtcyWgnbgD-GxVS.-78Fvf8S_Ji3uXbq?startTime=1702154801000

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
