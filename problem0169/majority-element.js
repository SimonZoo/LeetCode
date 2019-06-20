/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
  let obj = {},
    l = nums.length;
  for (let i = 0; i < l; i++) {
    let cur = nums[i];
    if (cur in obj) obj[cur]++;
    else obj[cur] = 1;
    if (obj[cur] > l / 2) return cur;
  }
};
