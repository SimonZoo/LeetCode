/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
  let l = nums.length,
    obj = {};
  for (let i = 0; i < l; i++) {
    let t = nums[i];
    if (t in obj) {
      delete obj[t];
    } else {
      obj[t] = 1;
    }
  }
  return Object.keys(obj)[0] - 0;
};
