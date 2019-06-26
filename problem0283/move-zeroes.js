/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
  let l = nums.length,
    k = 0;
  for (let i = 0; i < l; i++) {
    if (nums[i] != 0) {
      nums[k] = nums[i];
      k++;
    }
  }
  for (let i = k; i < l; i++) {
    nums[i] = 0;
  }
  return nums;
};
