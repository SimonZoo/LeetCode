/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
  let l = nums.length,
    sum = 0;
  for (let i = 0; i <= l; i++) {
    sum += i;
  }
  for (let i = 0; i < l; i++) {
    sum -= nums[i];
  }
  return sum;
};
