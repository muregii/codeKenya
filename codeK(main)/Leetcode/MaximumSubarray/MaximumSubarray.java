public class MaximumSubarray {
    // Method to find the maximum sum of a contiguous subarray
    public static int maxSubarray(int[] nums) {
        // Initialize variables to store the maximum sum
        int maxCurrent = nums[0]; // Initialize with the first element
        int maxGlobal = nums[0]; // Initialize with the first element
        
        // Iterate through the array starting from the second element
        for (int i = 1; i < nums.length; i++) {
            // Update maxCurrent to be the maximum of the current element or the sum of current element and maxCurrent
            maxCurrent = Math.max(nums[i], maxCurrent + nums[i]);
            // Update maxGlobal to be the maximum of maxGlobal and maxCurrent
            maxGlobal = Math.max(maxGlobal, maxCurrent);
        }
        
        // Return the maximum sum of the contiguous subarray
        return maxGlobal;
    }
    
    // Main method to test the maxSubarray method
    public static void main(String[] args) {
        // Test array
        int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        // Print the maximum sum of contiguous subarray
        System.out.println("Maximum sum of contiguous subarray: " + maxSubarray(nums));
    }
}

