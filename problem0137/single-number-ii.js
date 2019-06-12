/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
  let l = nums.length,
    obj = {};
  for (let i = 0; i < l; i++) {
    if (nums[i] in obj) {
      obj[nums[i]] += 1;
    } else {
      obj[nums[i]] = 1;
    }
  }
  for (key in obj) {
    if (obj[key] == 1) return key;
  }
};
