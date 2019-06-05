/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
  if (nums.length == 1) return nums[0];
  let max = nums[0],
    res = nums[0];
  for (let i = 1; i < nums.length; i++) {
    // compare cur_num and cur_num + max(last result)
    max = nums[i] > nums[i] + max ? nums[i] : nums[i] + max;
    res = res > max ? res : max;
  }
  return res;
};
