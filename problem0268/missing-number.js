/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
  if (nums.length == 1 && nums[0] == 0) return 1;
  nums.sort((a, b) => {
    return a - b;
  });
  let l = nums.length;
  for (let i = 0; i < l; i++) {
    if (i != nums[i]) return i;
  }
  return l;
};
