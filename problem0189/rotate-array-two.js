/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
  let l = nums.length;
  let moveK = k % l,
    count = 0;
  for (let start = 0; count < l; start++) {
    let cur = start,
      pre = nums[start];
    do {
      let next = (cur + moveK) % l,
        temp = nums[next];
      nums[next] = pre;
      pre = temp;
      cur = next;
      count++;
    } while (start != cur);
  }
};
