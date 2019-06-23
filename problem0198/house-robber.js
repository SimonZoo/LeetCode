/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
  let l = nums.length,
    sumEven = 0,
    sumOdd = 0;
  for (let i = 0; i < l; i++) {
    if (i % 2) {
      sumOdd += nums[i];
      sumOdd = Math.max(sumOdd, sumEven);
    } else {
      sumEven += nums[i];
      sumEven = Math.max(sumOdd, sumEven);
    }
  }
  return Math.max(sumOdd, sumEven);
};
