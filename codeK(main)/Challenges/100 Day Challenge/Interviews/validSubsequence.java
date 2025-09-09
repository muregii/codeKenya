/*
    VALIDATE SUBSEQUENCE

    Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.
    A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array.
    For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4].
    Note that a single number in an array and the array itself are both valid subsequences of the array.

    Sample Input
    array = [5, 1, 22, 25, 6, -1, 8, 10] 
    sequence = [1, 6, -1, 10]
    In this case return true
*/

//ZoomLink to the recorded interview: https://duke.zoom.us/rec/share/cR5c860VGT3C3jRZoRWWFUJEtAbFafFOrN1TCPXonNu75RPVC6krm93FukwhkfB1.fMu8zb5zYUk6-9Y0?startTime=1702150186000

import java.util.*;

class Program {
  public static boolean isValidSubsequence(
    List<Integer> array, List<Integer> sequence
  ) {
    // Write your code here.
     //sequence  array < array
    if (array.size() < sequence.size()) return false;

    for (int arrayNum : array){
        Integer sequenceNum = sequence.get(0);
      if (arrayNum == sequenceNum){
        sequence.remove(0);
      }
      if(sequence.size() == 0) return true;
  
    }
    return false;
    }
}
