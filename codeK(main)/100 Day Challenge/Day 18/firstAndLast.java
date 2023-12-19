/*
 * Given a sorted array of integers arr and an integer target,
 * find the index of the first and last position of target in arr.
 * If target can't be found in arr, return[-1,-1]
 * 
 * Example input: 
 * arr: [2,4,5,5,5,5,5,7,9,9]
 * target = 5;
 * output: [2,6]
 */

class FirstAndLast {
    public static void main (String[] args) {
        int[] arr = {2,4,5,5,5,5,5,7,9,9};
        int target = 5;
        int[] result = firstAndLast(arr, target);
        System.out.println("The output is " + result);
    }

    public static int[] firstAndLast(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != target) {
                left++;
            } else {
                break;
            }

        }
        for (int i = arr.length  - 1; i >= 0; i--) {
            if (arr[i] != target) {
                right--;
            } else {
                break;
            }
        }
        return new int[] {left,right};
    }
}
