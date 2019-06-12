/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
  let s = new Set(nums),
    sum = 0,
    l = nums.length;
  for (let item of s) {
    sum += 3 * item;
  }
  for (let i = 0; i < l; i++) {
    sum -= nums[i];
  }
  return sum / 2;
};
