#
Focuses on in place modification of arrays. while minimizing the number of times you have to write into the array.

Output: You should return the new length of the array after duplicates have been removed. Note that you don't need to actually resize the array; you just need to consider elements up to the returned length as the modified array.

Solve in linear time and constant space complexity, meaning usicreate array ingine.

Approach
1. Two pointers

Use two pointers: i and j. Pointer i is used to iterate over the array, and j is used to keep track of the position to place the next unique element.

Initially, set both i and j to 0.
Iterate over the array with i. Each time you find a new element (i.e., an element different from the previous one), copy it to the position indicated by j and increment j.

After the loop, j will be the new length of the array, and the first j elements in the array will be the unique elements.
