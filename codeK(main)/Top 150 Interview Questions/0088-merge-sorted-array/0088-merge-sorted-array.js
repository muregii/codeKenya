/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    let i = m - 1
    let j = n - 1
    let k = (m + n) - 1

    while(i>=0 && j>=0) {
        if (nums1[i] > nums2[j]) {
            nums1[k] = nums1[i]
            i--
        } else {
            nums1[k] = nums2[j]
            j--
        }
        k--
    }

    while(j>=0) {
        nums1[k] = nums2[j]
        j--
        k--
    }
};

// notes:
// pattern: 2 pointers
// why start from the end?
// Starting from the end ensures that we don't overwrite elements in nums1 that haven't been processed yet, and it allows us to perform the merging in-place without using additional space.
// time complexity of this solution is O(m + n).





