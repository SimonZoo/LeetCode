/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
  let a = 0,
    l = nums.length;
  for (let i = 0; i < l; i++) {
    a ^= nums[i];
  }
  return a;
};
