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

import java.util.*;

public class Firstandlast {
    // public int[] targetIndex(int[] arr, int target){
    //     Map<Integer, Integer> map = new HashMap<>();
       
    //     for(int i = 0; i < arr.length; i++){
    //         if(map.containsKey(target)){
    //             return new int[] {map.get(target), };
    //         }
    //         map.put(arr[i], i);
                 
    //     }
    // }

    public static int[] targetIndex(int[] arr, int target){
        int left = 0;
        int right = arr.length-1;
        int first = -1;
        int last = -1;
        
        
        while(left <= right){
         
            if(arr[left] == target) {
                first = left;
               break;
            }
            left++;
        }

        while(left <= right){
            if(arr[right] == target){
                last = right;
                break;
            }
            right--;
        }
            
        return new int[]{first, last};

    }
    public static void main(String[] args){
        
        int[] arr = {1, 2, 3, 3, 3, 3, 4, 4, 5, 6, 6};
        int[] result = Firstandlast.targetIndex(arr, 2);
        System.out.println(Arrays.toString(result));
    }
}
