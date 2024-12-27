/*
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
*/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 #include <stdlib.h>

int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int* arr = (int*)malloc(sizeof(int) * numsSize);
    if (!arr) 
        return NULL; 

    int leftProduct = 1;
    for (int i = 0; i < numsSize; i++) {
        arr[i] = leftProduct;
        leftProduct *= nums[i];
    }

    int rightProduct = 1;
    for (int i = numsSize - 1; i >= 0; i--) {
        arr[i] *= rightProduct;
        rightProduct *= nums[i];
    }

    return arr;
}
