/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
  let l = nums.length,
    cur = nums[0],
    count = 1;
  for (let i = 1; i < l; i++) {
    if (nums[i] == cur) count++;
    else count--;
    if (!count) {
      i++;
      cur = nums[i];
      count = 1;
    }
  }
  return cur;
};
