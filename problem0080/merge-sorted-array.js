/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
  for (let k = m + n - 1, i = m - 1, j = n - 1; k >= 0; k--) {
    if (i < 0) {
      nums1[k] = nums2[j];
      j--;
      continue;
    }
    if (j < 0) {
      nums1[k] = nums1[i];
      i--;
      continue;
    }

    if (nums1[i] > nums2[j]) {
      nums1[k] = nums1[i];
      i--;
    } else {
      nums1[k] = nums2[j];
      j--;
    }
  }
  return nums1;
};
